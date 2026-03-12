from pydobot import Dobot
import time

device = Dobot(port="COM3", verbose=True)
device.speed(50, 50)

def clamp(val, min_val, max_val):
    return max(min_val, min(val, max_val))

while True:
    try:
        x = input("x (150-300 mm, q to quit): ")
        if x.lower() == 'q':
            break
        y = float(input("y (-100 to 100 mm): "))
        z = float(input("z (20-200 mm): "))
        r = float(input("r (-90 to 90 deg): "))

        # Clamp coordinates
        x = clamp(float(x), 150, 300)
        y = clamp(float(y), -100, 100)
        z = clamp(float(z), 20, 200)
        r = clamp(float(r), -90, 90)

        # Move
        device.move_to(x, y, z, r, wait=True)
        time.sleep(0.5)  # pause to avoid soft lock

    except Exception as e:
        print("❌ Move failed:", e)

device.close()
