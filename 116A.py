n = int(input())
m = 0
list = []
for i in range (n):
    a,b = input().split()
    a=int(a)
    b=int(b)
    m -= a
    m+= b
    list.append(m)
print(max(list))