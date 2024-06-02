import pyautogui
import time
import math

# Define the parameters for the nested circles
center_x, center_y = 230, 400  # Center of the circles
max_radius = 90  # Maximum radius of the largest circle
num_circles = 16  # Number of nested circles
steps_per_circle = 66  # Number of steps (points) per circle
duration = 0.001  # Duration to move to each point
repeat_count = 100  # Number of times to repeat the nested circles pattern


def move_mouse_in_nested_circles(center_x, center_y, max_radius, num_circles, steps_per_circle, duration):
    k = 2
    for circle in range(num_circles):
        radius = (circle + k) * (max_radius / num_circles)
        for step in range(steps_per_circle):
            angle = 10 * math.pi * step / steps_per_circle
            x = center_x + int(radius * math.cos(angle))
            y = center_y + int(radius * math.sin(angle))
            pyautogui.moveTo(x, y, duration=0.0001)

        k = k+4
        if k >= 10:
            k = circle


# Move the mouse in nested circles a specific number of times
try:
    for k in range(repeat_count):
        move_mouse_in_nested_circles(center_x, center_y, max_radius, num_circles, steps_per_circle, duration)
        # time.sleep(0.05)  # Pause briefly before repeating
        if k % 5 == 0:
            time.sleep(10)
except KeyboardInterrupt:
    print("Mouse movement stopped by user")
