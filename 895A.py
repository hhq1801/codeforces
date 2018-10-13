n = int(input())
ls1 = input().split()
ls1 = [int(i) for i in ls1]
mangle = 180

def through(j):
    if j < n - 1:
        j = j + 1
    else:
        j = 0
    return (j)

for i in range(n):
    j = i
    angle = ls1[i]
    while True:
        j = through(j)
        angle += ls1[j]
        if angle >= 180:
            break
    mangle = min(abs(180 - angle), abs(180 - angle + ls1[j]), mangle)
    if mangle == 0:
        break

print(2 * mangle)
