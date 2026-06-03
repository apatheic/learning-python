# countdown.py - Simple Countdown Scenario

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

#Play an audio file when the countdown ends
subprocess.Popen(['start', 'alarm.wav'], shell=True)
