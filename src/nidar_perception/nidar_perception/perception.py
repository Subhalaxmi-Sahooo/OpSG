import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from rclpy.qos import qos_profile_sensor_data
class CameraViewer(Node):
    def __init__(self):
        super().__init__('camera_viewer')
        
        self.bridge = CvBridge()
        
        self.subscription = self.create_subscription(
            Image, 
            '/world/default/model/x500_depth_0/link/camera_link/sensor/IMX214/image',
            self.image_callback,
            qos_profile_sensor_data
        )
        
        self.get_logger().info("Camera Viewer Node has been started. Waiting for camera feed...")
    def image_callback(self, msg):
        try:
            current_frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            cv2.imshow("Camera Feed", current_frame)
            cv2.waitKey(30)
        except Exception as e:
            self.get_logger().error(f"Error converting image: {e}")
def main(args=None):
    rclpy.init(args=args)
    camera_viewer = CameraViewer()
    rclpy.spin(camera_viewer)
    camera_viewer.destroy_node()
    cv2.destroyAllWindows()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
            
        