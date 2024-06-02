import pyautogui
import time
import random

from main_click import click_kombat, click_test
from main_move import yes_coin_move

for i in range(1, 2500):
    click_test()
    yes_coin_move()
    if i % 10 == 0:
        t = random.choice([20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100])
        print("==> ", i, " Sleep: ", t)
        time.sleep(t)
    if i % 100 == 0:
        print(i, "i % 100 = ", i % 100)
        time.sleep(60)

    time.sleep(5)
    click_kombat()
