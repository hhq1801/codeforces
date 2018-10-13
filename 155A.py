n=int(input())
ls=input().split()
ls=[int(i) for i in ls]
ls1=[ls[0]]
count=0
for i in ls:
    if i>max(ls1) or i<min(ls1):
        count+=1
    ls1.append(i)
print(count)
