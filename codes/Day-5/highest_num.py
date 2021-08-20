# find the highest number from a list

# ls = int(input())
ls = [43, 21, 23, 65, 16, 44, 56]

temp = 0
for i in ls:
    if i > temp:
        temp = i

print(temp)
