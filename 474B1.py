n = int(input())
a = list(map(int,input().split()))
input()
q = list(map(int,input().split()))

k = []
for i in range(n):
    k += [i] * a[i]
print(k)
for i in q:
    print(k[i - 1] +1)