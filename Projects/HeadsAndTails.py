import random

options = ['heads', 'tails']

print('Guess the coin toss! (heads or tails)')
guess = input()

toss = random.choice(options) 

if guess == toss:
    print('You won!')
else:
    print(f'Nope! The coin landed on {toss}.')
