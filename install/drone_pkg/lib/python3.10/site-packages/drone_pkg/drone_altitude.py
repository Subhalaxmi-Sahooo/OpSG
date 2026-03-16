import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
class AltitudePublisher(Node):
    def __init__(self):
        super().__init__('altitude_publisher_node')
        self.publisher = self.create_publisher(Float64, 'drone_altitude', 10)
        self.timer=self.create_timer(timer_period_sec=1.0,callback=self.timer_callback)
        self.current_altitude=0.0
    def timer_callback(self):
        msg=Float64()
        msg.data=self.current_altitude
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing Altitude : {msg.data} meters')    
        self.current_altitude+=1.0
def main(args=None):
    rclpy.init(args=args)
    node= AltitudePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()