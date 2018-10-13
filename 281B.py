import math
from fractions import Fraction

x, y, n = input().split()
x = int(x)
y = int(y)
n = int(n)
new = 2

if y <= n:
    if Fraction(x, y) == int(Fraction(x, y)):
        print(str(Fraction(x, y)) + '/1')
    else:
        print(str(Fraction(x, y)))
else:
    for i in range(1, n + 1):
        frac = x / y
        up = frac * i
        up1 = math.ceil(up)
        up2 = math.floor(up)
        a = abs(Fraction(x, y) - Fraction(up1, i))
        b = abs(Fraction(x, y) - Fraction(up2, i))
        if a >= b and b < new:
            new = b
            uup = up2
            ddo = i
        elif a < b and a < new:
            new = a
            uup = up1
            ddo = i
    print(str(uup) + '/' + str(ddo))
