n,k=input().split()
n = int(n)
k = int(k)
list = input().split()
list1 = [int(i) for i in list]
m = list1[k-1]
count = 0
for i in list1:
    if i >= m and i >0:
        count +=1
print(count)