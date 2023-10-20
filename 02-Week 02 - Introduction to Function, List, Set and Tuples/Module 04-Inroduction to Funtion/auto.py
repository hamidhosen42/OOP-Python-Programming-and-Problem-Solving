import pyautogui
import time

# pyautogui.alert("This is an alert box")
time.sleep(5)

for i in range(1,5):
    time.sleep(1)
    pyautogui.write("I Love Python!",interval=0.25)
    pyautogui.press('enter')