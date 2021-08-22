import random
from sys import exit


number = random.randint(1, 100)
print(number)


while True:
    try:
        gussed_number = int(input('Guess a number: '))

        if gussed_number == number:
            print('Congratulations you have found the right number which is', number)
            break
        elif gussed_number > number:
            print('your gussed number is greater')
        else:
            print('your gusssed number is lower')
    except:
        print('Wrong input')
        exit(0)
