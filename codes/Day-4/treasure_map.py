row1 = ['🔥', '🔥', '🔥']
row2 = ['🔥', '🔥', '🔥']
row3 = ['🔥', '🔥', '🔥']

map = [row1, row2, row3]

# print(map)

pos = int(input())
r_pos = pos//10 - 1
c_pos = pos % 10 - 1
# print(f'{r_pos}\n{c_pos}')


map[r_pos][c_pos] = '🍆'


print(f'{row1}\n{row2}\n{row3}')
