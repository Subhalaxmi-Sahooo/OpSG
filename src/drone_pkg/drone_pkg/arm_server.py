import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool
class Arm_Server(Node):
    def __init__(self):
        super().__init__("arm_server_node")
        self.arm_service=self.create_service(SetBool, "arm_drone", self.arm_callback)
        self.get_logger().info("Arm Server is ready to receive requests.")
    def arm_callback(self, request, response):
        if request.data == True:
            self.get_logger().info("Arming the drone.")
            response.success = True
            response.message = "Drone armed successfully."
        else:
            self.get_logger().info("Disarming the drone.")
            response.success = True
            response.message = "Drone disarmed successfully."
        return response
def main(args=None):
    rclpy.init(args=args)
    arm_server = Arm_Server()
    rclpy.spin(arm_server)
    arm_server.destroy_node()
    rclpy.shutdown()
if __name__ == "__main__":
    main()