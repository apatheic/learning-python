import subprocess
calcProc = subprocess.Popen(['vim', '/home/fsociety/Documents/hello.txt'])

calcProc.poll() == None
#True
calcProc.wait()
#0
calcProc.poll()
#0
