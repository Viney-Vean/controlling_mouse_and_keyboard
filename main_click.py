import random

import pyautogui
import time

# Give yourself a few seconds to switch to the correct window
# time.sleep(5)

# List of coordinates to click
x_pos = 600
y_pos = 470
increase = 30
positions = [
    (x_pos, y_pos),
    (x_pos, y_pos + increase),
    (x_pos, y_pos + 2 * increase),
    (x_pos, y_pos + 3 * increase),
    (x_pos, y_pos + 4 * increase),
    (x_pos, y_pos + 5 * increase),
    (x_pos, y_pos + 6 * increase),

    (x_pos, y_pos),
    (x_pos, y_pos + increase),
    (x_pos, y_pos + 2 * increase),
]


def click_kombat():
    for position in positions:
        pyautogui.click(position[0], position[1])
        t = random.choice([1, 2, 3, 4, 5])
        time.sleep(1)  # Delay between clicks


def click_test():
    center_x, center_y = 50, 280
    for position in range(1, 3):
        pyautogui.click(center_x, center_y)
        t = random.choice([1, 2, 3, 4, 5])
        time.sleep(t)  # Delay between clicks
