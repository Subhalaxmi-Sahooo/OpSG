import rclpy 
from rclpy.node import Node
from std_srvs.srv import SetBool
class Arm_Client(Node):
    def __init__(self):
        super().__init__("arm_client_node")
        self.client_=self.create_client(SetBool, "arm_drone")
        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for the arm service to be available...")
        self.request_arm= SetBool.Request() 
    def send_request(self, arm):
            self.request_arm.data = arm
            self.get_logger().info(f"Sending request to arm the drone: {self.request_arm.data}")
            self.future = self.client_.call_async(self.request_arm)
            self.future.add_done_callback(self.response_callback)
    def response_callback(self, future):
            try:
                response = future.result()
                self.get_logger().info(f"Response received, success:{response.success}, message: {response.message}")
            except Exception as e:
                self.get_logger().error(f"Service call failed: {e}")
def main(args=None):
    rclpy.init(args=args)
    arm_client = Arm_Client()
    arm_client.send_request(True) 
    rclpy.spin(arm_client)
    arm_client.destroy_node()
    rclpy.shutdown()
if __name__ == "__main__":
    main()