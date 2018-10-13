m,n=input().split()
m=int(m)
n=int(n)
ls=input().split()
count=0
ls=[int(i) for i in ls]
for i in range(n-1):
    if ls[i+1]<ls[i]:
        count+=m

count+=ls[-1]

print(count-1)