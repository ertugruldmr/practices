import cmath

z = complex(input())
v = cmath.polar(z)
le = len(v)
i = 0
while i < le:
    print(v[i])
    i += 1