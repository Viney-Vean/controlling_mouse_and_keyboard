import pyautogui
import time
import random


def yes_coin_move():
    center_x, center_y = 50, 280
    to_down = 60
    duration = 0.5
    # Start
    pyautogui.moveTo(center_x, center_y)
    # Move to right 1
    x_to_right = center_x + 320
    pyautogui.moveTo(x_to_right, center_y, duration=duration)
    # Move down
    y_down = center_y + to_down
    pyautogui.moveTo(x_to_right, y_down, duration=duration)
    # to left 2
    pyautogui.moveTo(center_x, y_down, duration=duration)
    # Move down
    y_down = y_down + to_down
    pyautogui.moveTo(center_x, y_down, duration=duration)
    # Move to right
    pyautogui.moveTo(x_to_right, y_down, duration=duration)
    # # Move down
    y_down = y_down + to_down
    pyautogui.moveTo(center_x, y_down, duration=duration)
    # # to left
    pyautogui.moveTo(x_to_right, y_down, duration=duration)
    # # Move down
    y_down = y_down + to_down
    pyautogui.moveTo(center_x, y_down, duration=duration)
    # Move to right
    pyautogui.moveTo(x_to_right, y_down, duration=duration)

#
# for i in range(1, 2500):
#     test()
#     if i % 10 == 0:
#         t = random.choice([20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100])
#         print("==> ", i, " Sleep: ", t)
#         time.sleep(t)
#     if i % 100 == 0:
#         print(i, "i % 100 = ", i % 100)
#         time.sleep(50)
