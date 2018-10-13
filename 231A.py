n = int(input())
count= 0
for i in range(n):
    list = input().split()
    list = [int(i) for i in list]
    if sum(list)>=2:
        count +=1
print(count)
