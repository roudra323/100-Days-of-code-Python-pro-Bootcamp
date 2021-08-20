name1 = input()
name2 = input()
name = name1 + name2
name.lower()


t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')

ans = 0

if t and r and u and e and l and o and v and e:
    ans = str(t+r+u+e) + str(l+o+v+e)

print(ans)