n = int(input())
l = []
it = []
for i in range(n):
    l.append(1)
for i in range(n):
    it.append(l)
for i in range(1, n):
    m = it[i]
    for k in range(1, n):
        m[k] = m[k - 1] + it[i - 1][k]
print(it[0][n - 1])
