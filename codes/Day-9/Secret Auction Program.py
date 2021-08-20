# bidding programme


from time import sleep
from os import system, name
import operator
dic = {}


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


while True:
    key = input('Name: ')
    value = int(input())
    clear()

    dic[key] = value

    su = input('Wanna Continue?: ')
    if su == 'Y':
        continue
    else:
        break


sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
# import only system from os

# import sleep to show output for some time period

# define our clear function


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


print(f'Winner is {sorted_dic[0][0]} and money is {sorted_dic[0][1]}')
