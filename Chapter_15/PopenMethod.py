import subprocess
calcProc = subprocess.Popen(['vim', '/home/fsociety/Documents/hello.txt'])

calcProc.poll() == None
#True
calcProc.wait()
#0
calcProc.poll()
#0

with open('hello.txt', 'w') as file:
    file.write("Hello, World!")
    #12

subprocess.Popen(['cat', 'hello.txt'], shell=True) #also instead 'see' we can use 'start' for Windows, and 'open' for OS X
