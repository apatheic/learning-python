import random

randomNumber=random.randint(0,20)
print('i made a number from 0 to 20, try to guess.')
for i in range(6):
    try:
        guess=int(input())
        if guess<randomNumber:
            print('My number was bigger.')
        elif guess>randomNumber:
            print('My number was smaller.')
        else:
            print('You win!')
            break
    except:
        print('You can enter only integer nums!')
        continue
