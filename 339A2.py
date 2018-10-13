s = input()
fq = 4 * [0]  # 数组，第一个不用，本质上还是list

for i in range(0, len(s), 2):
    fq[int(s[i])] += 1

ns = ''
for i in range(1, 4):
    while fq[i] > 0:
        fq[i] -= 1
        ns += str(i)

print('+'.join(ns))
