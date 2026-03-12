# -----------------------------
# Dobot Magician Usage Notes
# -----------------------------
# Motion limits (safe workspace):
#   x: 150 mm to 300 mm  → forward/backward
#   y: -100 mm to 100 mm → left/right
#   z: 20 mm to 200 mm   → up/down
#   r: -90° to 90°       → end-effector rotation (around vertical axis)
#
# End-effector (pneumatic gripper):
#   - device.set_end_effector_suction(True)  → grip object (turn vacuum ON)
#   - device.set_end_effector_suction(False) → release object (turn vacuum OFF)
#
# Safety tips:
#   - Keep x, y, z, r within limits to avoid collisions
#   - Make sure teaching mode is OFF (arm stiff)
#   - E-stop released (twist red button if pressed)
#   - Start with small movements before testing full range


# ============ MAIN CODE (DO NOT TOUCH) ============
from pydobot import Dobot
import time

device = Dobot(port="COM3", verbose=True)

# Speed (required)
device.speed(100, 50)

# Input loop
while True:
    x = input("x (mm, q to quit): ")
    if x.lower() == 'q':
        break
    y = input("y (mm): ")
    z = input("z (mm): ")
    r = input("r (deg): ")

    try:
        device.move_to(float(x), float(y), float(z), float(r), wait=False)
    except Exception as e:
        print("Move failed:", e)

device.close()