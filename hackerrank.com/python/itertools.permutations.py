from itertools import permutations
inp = input().split()
lst, num = inp[0], int(inp[1])
l = list(permutations(lst, num))
r = []
for i in range(len(l)):
    r.append(''.join(list((l[i]))))
r.sort()
for i in range(len(r)):
    print(r[i])