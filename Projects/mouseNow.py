# mouseNow.py - print position your mouse.

import pyautogui
print('For exit press keys <Ctrl+C>.')

try:
    while True:
        x, y = pyautogui.position()
        positionStr = f'X: {str(x).rjust(4)} Y: {str(y).rjust(4)}'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('\nDone.')
