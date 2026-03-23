Week 0 CAD tasks: https://cad.onshape.com/documents/0179b728dd6cf5fdf34f7db9/w/5ec6f882f6f17e066df61fff/e/34a0e73822ab7b1169921801?renderMode=0&uiState=69b818e731e57fabf685e355

Week 1 CAD tasks: https://cad.onshape.com/documents/5965ec15bfa2bc3e1a299ad8/w/73ec7f2d4e9b4e7990dcfa00/e/2f9693361ea22826409942b2?renderMode=0&uiState=69c1876cfed5b8f664958f64

Drone Architecture & Frame Selection

To meet the requirements of a high-agility scout drone, the following hardware configuration has been selected. This setup prioritizes a lightweight profile, structural rigidity, and an unobstructed field of view (FOV) for Search and Rescue (SAR) operations.

1. Multirotor Configuration: Quadcopter

While Hexacopters and Octocopters offer motor redundancy and higher lift capacity, they require significantly larger batteries and heavier frames. For a scout drone where light-weightedness and flight endurance are the primary constraints, a Quadcopter is the most efficient choice. It offers the best thrust-to-weight ratio and simplifies the mechanical build.

2. Frame Geometry: The Deadcat

Within the quadcopter category, the shape of the frame dictates its utility. 

-The H-Frame: The central body is a long rectangle, with arms protruding straight out from the sides. 

Pros: Massive amounts of room for electronics, batteries, and large camera payloads along the central bus. 

Cons: Heavier than an X-frame and slightly less structurally rigid at the arm joints during a crash. 

-The True-X Frame: The motors form a perfect square, with the arms crossing at exactly 90 degrees in the center. 

Pros: Perfectly balanced. The Center of Gravity (CG) and Center of Thrust (CT) are identical. Incredibly agile. 

Cons: The front two propellers will constantly be in the video feed of a forward-facing camera. 

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
 
5. Material Selection

To achieve the "light-weightedness" mandate while maintaining the structural rigidity necessary for high-speed SAR operations, the drone relies on a specialized, hybrid material approach:

-Primary Airframe (Carbon Fiber): The bottom plate, top plate, and Deadcat arms are machined from 3K twill carbon fiber. Carbon fiber offers an unmatched stiffness-to-weight ratio, ensuring the frame remains rigid and free of resonance even under high thrust loads.

-Sensor Mounts (TPU): Rather than using heavy mechanical gimbals, the oblique camera housing, GPS seat, and antenna mounts are 3D printed using TPU (Thermoplastic Polyurethane). TPU is highly durable, lightweight, and natively absorbs high-frequency motor vibrations, acting as an integrated shock absorber for the camera feed.

-Fasteners & Hardware: To eliminate parasitic weight, standard steel hardware is replaced with knurled aluminum standoffs and titanium alloy screws where structural integrity allows.

Camera Selection for Area Scanning

Camera comparison table : https://docs.google.com/spreadsheets/d/157Fvjwuyvo4Nkn1HNT_8Oc1bsEw7guuEHJ5BnLttx_k/edit?usp=sharing

<img width="1338" height="167" alt="image" src="https://github.com/user-attachments/assets/2739d2be-9f73-4fb7-8f8c-7bd06782547a" />

While the Raspberry Pi Camera V3 is the safest fallback, the Arducam 16MP Autofocus remains the superior choice for this specific architecture. It provides the exact middle-ground needed: it utilizes the low-overhead MIPI CSI-2 interface to communicate with the onboard computer, weighs practically nothing (5g), and offers double the pixel density of the standard Pi V2 camera, ensuring the detection algorithms have enough high-contrast edge data to identify targets from a 30m-40m altitude over the 30-hectare search grid.

Alternatively, if the onboard computer struggles with the OpenCV workload during initial bench testing, the Luxonis OAK-1-Lite should be documented as the immediate contingency plan, as it offloads all vision processing directly onto the camera hardware.

Motor and ESC 

To maintain high agility and handle wind resistance during the scanning mission, the propulsion system needs to comfortably lift the 600g–800g target All-Up Weight (AUW) with a minimum 3:1 thrust-to-weight ratio, all while drawing minimal current.

Three different motor options were analyzed based on stator size and KV rating for a 4S battery setup. The iFlight XING2 1404 (4600KV) is incredibly light at 9g, but only produces around 450g of thrust per motor. Four of these would provide roughly 1800g of total thrust, yielding just over a 2:1 ratio. The drone would struggle to recover from descents, and the motors would need to run at 70% throttle just to maintain a hover, drastically reducing efficiency. On the heavier end, the BrotherHobby VY 2004 (3150KV) produces a massive 720g of thrust but draws up to 16.5A, pulling too much current for sustained endurance flights.

For the Electronic Speed Controllers (ESCs), the Diatone Mamba 25A, SpeedyBee 30A Mini, and Hobbywing XRotor 40A were compared. The 25A rating on the Mamba offers a slightly smaller thermal safety margin for continuous 15-20 minute flights. Conversely, the 40A Hobbywing board is massive overkill for the low-amp motors required and adds unnecessary parasitic weight to the frame.

Conclusion: The EMAX Eco II 2004 (2400KV) motors paired with the SpeedyBee 30A Mini 4-in-1 ESC should be utilized. The 2004 stator size provides the ideal balance of torque and weight for a 5-inch endurance build. The 2400KV variant maximizes cruising efficiency (yielding about 6.2 g/W) while still generating a total of ~2400g of thrust, perfectly hitting the 3:1 ratio requirement. These motors pull a maximum of 12.8A at 100% throttle. The SpeedyBee 30A ESC provides more than double that required capacity, ensuring the components will remain cool even under heavy wind loads. Using a 4-in-1 layout centralizes the weight at just 5.5g and keeps the carbon fiber arms clean to reduce aerodynamic drag.



