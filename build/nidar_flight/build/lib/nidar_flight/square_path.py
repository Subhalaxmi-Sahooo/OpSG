import rclpy
from rclpy.node import Node
from px4_msgs.msg import VehicleOdometry, OffboardControlMode, TrajectorySetpoint, VehicleCommand
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
import math
from nidar_flight.takeoff_node import TakeoffNode
class SquarePathNode(TakeoffNode):
    def __init__(self):
        super().__init__()
        self.get_logger().info("SquarePathNode initialized")
        
        self.current_x=0.0
        self.current_y=0.0
        self.current_z=0.0
        
        #qos profile configuration
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            durability=DurabilityPolicy.VOLATILE,
            depth=1
        )
        
        #Subscriber to odometry topic 
        self.odom_subscriber = self.create_subscription(
            VehicleOdometry,
            '/fmu/out/vehicle_odometry',
            self.odom_callback,
            qos_profile
        ) 

        #square waypoints definition
        self.square_waypoints= [
            [0.0, 0.0, 0.0],  # Takeoff point
            [0.0, 0.0, self.target_height],
            [10.0, 0.0, self.target_height],
            [10.0, 10.0, self.target_height],
            [0.0, 10.0, self.target_height],
            [0.0, 0.0, self.target_height]  # Return to starting point of square
        ]
        self.current_waypoint_index=0
        
    #callback to update current position from odometry data
    def odom_callback(self, msg):
        self.current_x = msg.position[0]
        self.current_y = msg.position[1]
        self.current_z = msg.position[2]
    def publish_waypoint_setpoint(self, target, yaw):
        msg = TrajectorySetpoint()
        msg.position = [float(target[0]), float(target[1]), float(target[2])] # NED notation 
        msg.yaw=float(yaw)
        msg.yawspeed=float('nan')  # Set yawspeed to NaN to ignore yaw rate control 
        msg.acceleration = [float('nan'), float('nan'), float('nan')]  # Set acceleration to NaN to ignore acceleration control
        msg.velocity = [float('nan'), float('nan'), float('nan')]  # Set velocity to NaN to ignore velocity control
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.trajectory_setpoint_pub.publish(msg)
    #timer callback to publish offboard control mode 
    def timer_callback(self):
        self.publish_offboard_control_mode() 
        target = self.square_waypoints[self.current_waypoint_index]
        if self.current_waypoint_index == 0 or self.current_waypoint_index == 1: 
            target_yaw = 0.0 # Keep it facing North during takeoff and hover
        else: 
            # Look at the previous corner, and the next corner, to draw a perfect straight line
            prev_target = self.square_waypoints[self.current_waypoint_index - 1]
            target_yaw = math.atan2(target[1] - prev_target[1], target[0] - prev_target[0])
        self.publish_waypoint_setpoint(target, target_yaw)       
        
        if self.timer_count == 20: # After 2 seconds, arm vehicle and hand control over to the offboard mode
            self.get_logger().info('Engaging offboard mode...')
            self.engage_offboard_mode()
        if self.timer_count == 30:
            self.get_logger().info('Arming vehicle...')
            self.arm_vehicle()
        if self.timer_count > 30: # After arming, start navigating through the square waypoints
        
            #distance calculation to current waypoint
            distance = math.sqrt((target[0] - self.current_x) ** 2 +
                                (target[1] - self.current_y) ** 2 )
                                
            #if within 2.5 meters of the target waypoint, move to the next waypoint
            if distance <2.5:
                if self.current_waypoint_index < len(self.square_waypoints) - 1:
                    self.current_waypoint_index += 1
                    self.get_logger().info(f"Moving to waypoint {self.current_waypoint_index}: {self.square_waypoints[self.current_waypoint_index]}")
                else:
                    self.get_logger().info("Completed square path. Returning to takeoff point.")
                    self.current_waypoint_index = 0 #starting point of square is index 1, index 0 is takeoff point, this statement lands the drone after completing the path
        self.timer_count +=1

def main(args=None):
    rclpy.init(args=args)
    square_path_node = SquarePathNode()
    rclpy.spin(square_path_node)
    square_path_node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()