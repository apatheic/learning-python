# stopwatch.py - simple program-chronometer

import time

#Displaying instructions for using the program
print('To start the countdown, press the Enter key. Subsequently, to simulate the clicks of the stopwatch button, press the key. To exit the program, press the keys.')
input() #Keystroke <Enter> start countdown

print('Countdown start.')
start = time.time() # Getting time first dimension

lastTime = start
lapNum = 1

#Start tracking measurements.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - start, 2)
        print('Dismension #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() #reset the time of the last measurement

except KeyboardInterrupt:
    #handle the exception to prevent its messages from being displayed.
    print('\nDone.')
