

size = input()
pep = input()
chese = input()

price = 0
temp = 0


def add_pep_s(price):
    price += 2
    return price


def add_pep_lm(price):
    price += 3
    return price


def extra_chese(price):
    price += 1
    return price


if size == 'S':
    price = 15
    if pep == 'Y':
        temp = add_pep_s(price)
    if chese == 'Y':
        temp = extra_chese(price)

elif size == 'M':
    price = 20
    if pep == 'Y':
        temp = add_pep_lm(price)
    if chese == 'Y':
        temp = extra_chese(price)

else:
    price = 25
    if pep == 'Y':
        temp = add_pep_lm(price)
    if chese == 'Y':
        temp = extra_chese(price)


print(temp)
