import pyautogui

pyautogui.size()
#1920x1080

width, height = pyautogui.size()

pyautogui.FAILSAFE = False

print(pyautogui.position())
#(311, 622)
