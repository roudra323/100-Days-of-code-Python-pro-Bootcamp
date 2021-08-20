# toss

import random
test_seed = int(input())
random.seed(test_seed)

toss = random.randint(0, 1)

if toss == 1:
    print('Head')
else:
    print("Tail")
