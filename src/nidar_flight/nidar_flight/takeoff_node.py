import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from px4_msgs.msg import OffboardControlMode, TrajectorySetpoint, VehicleCommand
class TakeoffNode(Node):
    def __init__(self):
        super().__init__('takeoff_node')
        self.target_height = 10.0
        
        #PX4 compatible QoS profile for offboard control 
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability= DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )
        
        self.offboard_control_mode_pub = self.create_publisher(OffboardControlMode, '/fmu/in/offboard_control_mode', qos_profile)
        self.trajectory_setpoint_pub = self.create_publisher(TrajectorySetpoint, '/fmu/in/trajectory_setpoint', qos_profile)
        self.vehicle_command_pub = self.create_publisher(VehicleCommand, '/fmu/in/vehicle_command', qos_profile)
        
        #10 Hz timer to publish setpoints
        self.timer=self.create_timer(0.1, self.timer_callback)
        self.timer_count=0
    def timer_callback(self):
        # Publish offboard control mode and trajectory setpoint for takeoff
        self.publish_offboard_control_mode()
        self.publish_trajectory_setpoint()
        
        if self.timer_count == 20: # After 2 seconds, arm vehicle and hand control over to the offboard mode
            self.get_logger().info('Engaging offboard mode...')
            self.engage_offboard_mode()
        if self.timer_count == 30:  
            self.get_logger().info('Arming vehicle...')
            self.arm_vehicle()
        if self.timer_count == 150: # After 15 seconds, disarm the vehicle
            self.get_logger().info('Hover complete. Initiating landing...')
            self.land_vehicle()
        if self.timer_count == 200: # After 20 seconds, shutdown the node
            self.get_logger().info('Mission complete. Shutting down takeoff node...')
            raise SystemExit
        self.timer_count += 1
    def publish_offboard_control_mode(self):
        msg = OffboardControlMode()
        msg.position = True # Enable position control
        msg.velocity = False # Disable velocity control
        msg.acceleration = False # Disable acceleration control
        msg.attitude = False # Disable attitude control
        msg.body_rate = False # Disable body rate control
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)  # Convert to microseconds
        self.offboard_control_mode_pub.publish(msg)
        
    def publish_trajectory_setpoint(self):
        msg = TrajectorySetpoint()
        msg.position = [0.0, 0.0, self.target_height]  # NED notation, Set target position (x, y, z), z is negative for takeoff, Index 0 is X (North), Index 1 is Y (East), Index 2 is Z (Down)
        msg.yaw=0.0
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)  
        self.trajectory_setpoint_pub.publish(msg)
    
    def arm_vehicle(self):
        msg = VehicleCommand() 
        msg.command = VehicleCommand.VEHICLE_CMD_COMPONENT_ARM_DISARM #corresponds to the integer value 400 in the MAVLink protocol, which is used to arm or disarm the vehicle.
        msg.param1 = 1.0  # 1.0 means arm
        msg.target_system = 1 # The target system ID (usually 1 for the main vehicle)
        msg.target_component = 1 # The target component ID (usually 1 for the main component)
        msg.source_system = 1 # The source system ID (usually 1 for the main system)
        msg.source_component = 1 # The source component ID (usually 1 for the main component)
        msg.from_external = True # Indicates that the command is coming from an external source
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.vehicle_command_pub.publish(msg)
    
    def engage_offboard_mode(self):
        msg = VehicleCommand()
        msg.command = VehicleCommand.VEHICLE_CMD_DO_SET_MODE #corresponds to the integer value 176 in the MAVLink protocol, which is used to set the flight mode of the vehicle.
        msg.param1 = 1.0  # Custom mode
        msg.param2 = 6.0  # PX4 custom mode for offboard (6 corresponds to OFFBOARD mode in PX4)
        msg.target_system = 1
        msg.target_component = 1
        msg.source_system = 1
        msg.source_component = 1
        msg.from_external = True
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.vehicle_command_pub.publish(msg)
    
    def land_vehicle(self):
        msg = VehicleCommand()
        msg.command = VehicleCommand.VEHICLE_CMD_NAV_LAND #corresponds to the integer value 21 in the MAVLink protocol, which is used to command the vehicle to land.
        msg.target_system = 1
        msg.target_component = 1
        msg.source_system = 1
        msg.source_component = 1
        msg.from_external = True
        msg.timestamp = int(self.get_clock().now().nanoseconds / 1000)
        self.vehicle_command_pub.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node = TakeoffNode()
    try:
        rclpy.spin(node)
    except SystemExit:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
if __name__ == '__main__':
    main()