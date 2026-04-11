import os 

path = '/home/user/'
totalSize = 0

for filename in os.listdir(path):
    totalSize += os.path.getsize(os.path.join(path, filename))
print(totalSize)
