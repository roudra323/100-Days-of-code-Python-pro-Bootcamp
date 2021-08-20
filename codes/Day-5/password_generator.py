import random

st = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

str2 = ['!', '"', '#', '$', '%', '&', '(', '*', '+', '/', ')']


password = ''

for i in range(10):
    temp = random.choice(st)
    password += temp
    temp2 = random.choice(str2)
    password += temp2

print(''.join(set(password)))
