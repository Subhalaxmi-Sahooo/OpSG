Week 0 CAD tasks: https://cad.onshape.com/documents/0179b728dd6cf5fdf34f7db9/w/5ec6f882f6f17e066df61fff/e/34a0e73822ab7b1169921801?renderMode=0&uiState=69b818e731e57fabf685e355

Week 1 CAD tasks: https://cad.onshape.com/documents/5965ec15bfa2bc3e1a299ad8/w/73ec7f2d4e9b4e7990dcfa00/e/2f9693361ea22826409942b2?renderMode=0&uiState=69c1876cfed5b8f664958f64

Drone Architecture & Frame Selection

To meet the requirements of a high-agility scout drone, the following hardware configuration has been selected. This setup prioritizes a lightweight profile, structural rigidity, and an unobstructed field of view (FOV) for Search and Rescue (SAR) operations.

1. Multirotor Configuration: Quadcopter

While Hexacopters and Octocopters offer motor redundancy and higher lift capacity, they require significantly larger batteries and heavier frames. For a scout drone where light-weightedness and flight endurance are the primary constraints, a Quadcopter is the most efficient choice. It offers the best thrust-to-weight ratio and simplifies the mechanical build.

2. Frame Geometry: The Deadcat

Standard "True-X" frames are excellent for racing but suffer from "prop-in-view," where the propellers obstruct the camera feed. To solve this without adding the weight of a complex gimbal or a massive H-frame, we are utilizing a Deadcat Frame.

- Geometry: The front arms are swept wider apart (approx. 140°) and pushed back, while the rear arms remain closer together.

- Visibility: This wide-angle stance ensures that even during aggressive forward pitch, the propellers stay completely out of the camera's FOV.

- Weight Efficiency: It maintains the structural rigidity of an X-frame while providing the elongated body of an H-frame for battery and electronics mounting.

- Balance Note: Because the Center of Thrust is shifted rearward, the battery is positioned toward the back of the frame to keep the Center of Gravity (CG) perfectly centered.

3. Sensor Integration: Oblique vs. Nadir

The Choice: Oblique (45°–60°) on a Deadcat Frame
An oblique angle is the requirement for SAR. It allows the operator to identify human profiles rather than just "top-of-head" blobs and provides much better depth perception when navigating 30-hectare search zones at high speeds while also being able to see the path ahead and not just scan the area which helps in obstacle avoidance.

4. Target Geolocation & Mathematical Offset

Since the camera is tilted at an angle (θ), the drone's GPS coordinate will not be directly over the target. To ensure accurate mapping, the system calculates the horizontal offset (d) in real-time using the drone's altitude (h) and the camera's pitch angle (θ) via the tangent projection formula:
d=h⋅tan(θ)

By combining the drone’s current GPS heading with this calculated distance (d), the software automatically generates the precise coordinates of any detected object on the ground.
 

