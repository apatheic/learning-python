import os
import shutil

os.makedirs('Scripts', exist_ok=True)
os.makedirs('Logs', exist_ok=True)
for folderName, subfolders, filenames in os.walk('test_garbage'):
    for filename in filenames:
        oldPath = os.path.join(folderName, filename)
        if filename.endswith('.py'):
            destination = 'Scripts'
        elif filename.endswith('.pdf') or filename.endswith('.txt'):
            destination = 'Logs'
        else:
            continue
        print(f'Moving {filename} from {folderName} to {destination}')
        shutil.move(oldPath, destination)
