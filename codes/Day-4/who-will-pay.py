# who is paying ?
import random

seed = int(input())
random.seed(seed)

names_as_csv = input()

name_list = names_as_csv.split(', ')


print(name_list[random.randint(0, len(name_list)-1)])
