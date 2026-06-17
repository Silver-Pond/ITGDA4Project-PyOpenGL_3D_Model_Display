Question 1 - 3D Model Display (PyOpenGL)

Requirements:
- Python 3.x
- pygame
- PyOpenGL
- PyOpenGL_accelerate (optional but recommended)

Install dependencies:
- pip install pygame PyOpenGL PyOpenGL_accelerate

How to Run:
1. Open the IDE of your choice, for me its PyCharm
<img width="1920" height="1080" alt="Screenshot (185)" src="https://github.com/user-attachments/assets/be51024f-3450-4c6c-a6a0-e0831ea4c1b1" />

2. Press on the "Open" button on the top and select the folder
<img width="1920" height="1080" alt="Screenshot (186)" src="https://github.com/user-attachments/assets/7be5b949-459b-4ab0-b60d-4b64cebee8e9" />

3. Press the green play button at the top and run python q1_display.py
<img width="1920" height="1080" alt="Screenshot (187)" src="https://github.com/user-attachments/assets/fde780ed-fb00-4ea5-b951-b24886eba78f" />

Controls:
- SPACE → Cycle between Cube, Pyramid, and Prism
- Close window to exit

Notes:
- Models are centred at origin.
- Camera is positioned at z = -6 to avoid being inside the model.
===============================================================================================

Question 2 – Translation Controls

Model Cycling:
- SPACE → Cycle between Cube, Pyramid, and Prism

Translation Controls:

- X-axis:
   - D → Move Positive X
   - A → Move Negative X

- Y-axis:
  - W → Move Positive Y
  - S → Move Negative Y

- Z-axis:
  - Q → Move Positive Z
  - E → Move Negative Z

Note:
- When models are cycled, the new model remains in the same translated position.
===============================================================================================

Question 3 – Colour Feature

Press C → Toggle colored surfaces ON/OFF

Notes:
- Edges remain white.
- Surfaces are solid and not transparent.
===============================================================================================

Question 4 – Texture Feature

Press C → Cycle rendering modes:
- 0 → Wireframe
- 1 → Colored
- 2 → Textured

Notes:
- Texture image file included in submission.
- Previous features (translation, rotation, swapping) remain functional.
===============================================================================================

Question 5 – Textured With Color Tint Feature

Model Cycling:
- SPACE → Cycle between Cube, Pyramid, and Prism

Translation Controls:

- X-axis:
   - D → Move Positive X
   - A → Move Negative X

- Y-axis:
  - W → Move Positive Y
  - S → Move Negative Y

- Z-axis:
  - Q → Move Positive Z
  - E → Move Negative Z

Press C → Cycle rendering modes:
- 0 → Wireframe
- 1 → Colored
- 2 → Textured
- 3 → Textured with color tint
===============================================================================================
