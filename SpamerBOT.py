from pyautogui import typewrite, press
from time import sleep

message = input("Enter a messge")
renge = int(input("Enter range:"))

sleep(7)
for i in range(renge):
    typewrite(message)
    press("Enter")

