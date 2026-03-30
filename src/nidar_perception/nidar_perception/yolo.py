import rclpy 
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO

class HumanDetector(Node):
    def __init__(self):
        super().__init__('human_detector')
        
        self.bridge = CvBridge()
        
        self.get_logger().info("Loading YOLOv8 model...")
        
        self.model = YOLO('yolov8n.pt')  # Load the YOLOv8 model
        self.get_logger().info("YOLOv8 model loaded successfully. Waiting for camera feed...")
        
        #  publish to the topic /human_detection - x, y, confidence
        self.publisher_ = self.create_publisher(Point, '/human_detection', 10)
        
        # Subscribe to the camera feed
        self.subscription = self.create_subscription(
            Image,
            '/world/default/model/x500_depth_0/link/camera_link/sensor/IMX214/image',
            self.image_callback,
            10)
    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding = 'bgr8')
            results = self.model(cv_image, classes= [0], conf= 0.5, verbose = False)
            
            for r in results:
                for box in r.boxes:
                    for box in r.boxes:
                        # Use .tolist() to perfectly extract 4 pure Python floats
                        x1, y1, x2, y2 = box.xyxy[0].tolist()
                        
                        # Use .item() to extract the single pure confidence float
                        confidence = box.conf[0].item()
                        
                        # Calculate the center of the bounding box
                        center_x = (x1 + x2) / 2.0
                        center_y = (y1 + y2) / 2.0
                        
                        # Publish the detection as a Point message
                        point_msg = Point()
                        point_msg.x = center_x
                        point_msg.y = center_y
                        point_msg.z = confidence 
                        self.publisher_.publish(point_msg)
                        
                        # Draw the bounding box and confidence on the image
                        cv2.rectangle(cv_image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                        cv2.putText(cv_image, f'Human : {confidence:.2f}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            # Display the image with detections
            cv2.imshow('YOLOv8 Human Detection', cv_image)
            cv2.waitKey(30)
        except Exception as e:
            self.get_logger().error(f"Error processing image: {e}")
def main(args=None):
    rclpy.init(args=args)
    human_detector = HumanDetector()
    rclpy.spin(human_detector)
    human_detector.destroy_node()
    cv2.destroyAllWindows()
    rclpy.shutdown()                        
if __name__ == '__main__':
    main()
    
                       
        
        
        