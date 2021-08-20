import random
user_input = int(input('press 0 for paper, 1 for scessor, 2 for rock\n'))

com = [0, 1, 2]
ch_com = random.choice(com)
print(ch_com)

if user_input == 0 and ch_com == 2:
    print('You Win')
elif user_input == 2 and ch_com == 1:
    print('You Win')
elif user_input == 1 and ch_com == 0:
    print('You Win')
else:
    print("You lost")
