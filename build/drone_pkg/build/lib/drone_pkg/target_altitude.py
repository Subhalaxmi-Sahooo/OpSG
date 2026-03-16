import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
class Altitude_Subscriber(Node):
    def __init__(self):
        super().__init__("altitude_subsrciber_node")
        
        self.subscription = self.create_subscription(Float64, "drone_altitude", self.altitude_callback, 10)
    def altitude_callback(self, msg):
        self.get_logger().info(f"Received Altitude : {msg.data} meters")
        
def main(args=None):
    rclpy.init(args=args)
    node = Altitude_Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == "__main__":
    main()