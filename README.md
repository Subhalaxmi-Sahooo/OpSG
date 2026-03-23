Week 0 CAD tasks: https://cad.onshape.com/documents/0179b728dd6cf5fdf34f7db9/w/5ec6f882f6f17e066df61fff/e/34a0e73822ab7b1169921801?renderMode=0&uiState=69b818e731e57fabf685e355

Week 1 CAD tasks: https://cad.onshape.com/documents/5965ec15bfa2bc3e1a299ad8/w/73ec7f2d4e9b4e7990dcfa00/e/2f9693361ea22826409942b2?renderMode=0&uiState=69c1876cfed5b8f664958f64

1. Multirotor Configurations: Quad vs. Hex vs. Octo 

    Hexacopters & Octocopters (6 or 8 motors): These are built for heavy lifting and redundancy. If a motor fails, the drone can still land safely. However, they require massive batteries, more electronic components, and are inherently heavy. 

    Quadcopters (4 motors): The standard for lightweight, agile platforms. They are mathematically simple, require fewer parts, and maximize flight time by minimizing the raw weight of the motors and frame. 

For a scout drone where "light-weightedness" is a primary requirement, a Quadcopter is the only logical choice. 

2. Quadcopter Frame Geometries 

Within the quadcopter category, the shape of the frame dictates its utility. 

    The True-X Frame: The motors form a perfect square, with the arms crossing at exactly 90 degrees in the center. 

    Pros: Perfectly balanced. The Center of Gravity (CG) and Center of Thrust (CT) are identical. Incredibly agile. 

    Cons: The front two propellers will constantly be in the video feed of a forward-facing camera. 

    The H-Frame: The central body is a long rectangle, with arms protruding straight out from the sides. 

    Pros: Massive amounts of room for electronics, batteries, and large camera payloads along the central bus. 

    Cons: Heavier than an X-frame and slightly less structurally rigid at the arm joints during a crash. 

    The Deadcat Frame: An asymmetrical X-frame. The front arms are swept wider apart and pushed slightly backward, resembling a splayed cat. 

    Pros: Completely removes the front propellers from the camera's field of view. Maintains excellent structural rigidity. 

    Cons: The Center of Thrust is shifted backward, meaning the Center of Gravity must also be actively shifted backward to match it, otherwise the rear motors overwork. 

The Deadcat Quadcopter is definitively the best choice for this specific surveillance architecture. It perfectly threads the needle between the three main constraints: 

    Camera Visibility: The wide front stance guarantees an unobstructed view. 

    Light-weightedness: It uses minimal material compared to an H-frame or Hexacopter. 

    Structural Stability: The central body can be made highly rigid. 

Option A: True-X Frame with Nadir (90°) Camera 

The True-X architecture positions motors in a symmetrical square, offering the highest baseline agility and straightforward Center of Gravity (CG) balancing. 

    Payload Integration: A Nadir (straight-down) camera avoids propeller obstruction natively. 

    Mission Constraints: A 90° downward angle introduces severe operational blindspots for Search and Rescue (SAR). It only captures the tops of targets, making profiles difficult to identify, especially under foliage. Furthermore, it eliminates the operator's forward visibility, significantly reducing the safe scanning speed across the 30-hectare area. 

Option B: Dead Cat Frame with Oblique (45°-60°) Camera 

The Dead Cat architecture modifies the True-X by sweeping the front arms outward (e.g., 140° apart) and pushing the Center of Thrust rearward. 

    Payload Integration: Accommodates an underslung Oblique camera. The wide front stance guarantees the spinning propellers remain completely out of the camera's field of view during forward pitch. 

    Mission Advantages: The 45° angle is the Search and Rescue standard. It captures target profiles, highlights shadows, provides visibility under tree canopies, and allows the operator to safely navigate obstacles at high speeds. 

    Design Requirements: Requires an elongated center plate to shift the battery rearward (balancing the shifted Center of Thrust) and extended landing gear to protect the underslung camera module. 

    Target Geolocation (The Offset Solution) 

    While an Oblique camera introduces a horizontal offset between the drone's GPS coordinate and the target's physical location, this is resolved programmatically. The target's exact coordinates will be calculated in real-time using the drone's altitude (h) and the camera's pitch angle (θ) via the tangent projection formula: d=h⋅tan(θ). 
Hence, the best choice would be a deadcat frame with an oblique camera.

 

