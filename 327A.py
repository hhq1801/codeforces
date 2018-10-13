#必须翻1次，翻了后，最大的一块全是1的有多大
n=int(input())
list=input().split()
list=[int(i) for i in list]
ls=[]
if n ==1:
    if list[0]==0: print(1)
    if list[0]==1: print(0)
else:
    for i in range(0,n-1):
        if list[i]!=list[i+1] and list[i]==0:
            ls.append(i+1)
        if list[i]!=list[i+1] and list[i]==1:
            ls.append(i+1)
    ls.append(n)
    if len(ls)==1:
        if list[0]==0:
            print(n)
        else: print(n-1)
    elif len(list)==2:
        print(n)
    else:
        ls1=[ls[0]]
        for i in range(1,len(ls)):
            ls1.append(ls[i]-ls[i-1])
        count=0
        for i in range(0,len(ls1)-2):
            count = max(ls1[i]+ls1[i+1]+ls1[i+2],count)
        print (count)
