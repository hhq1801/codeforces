import math

n, m, a = input().split()
n = int(n)
m = int(m)
a = int(a)
if a >= max(n, m):
    print(1)
else:
    print(math.ceil(n / a) * (math.ceil(m / a)))
