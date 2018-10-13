k,p =input().split()
k=int(k)
p=int(p)
a=0
for i in range(1,k+1):
    ls = []
    for j in range(len(str(i))):
        ls.append(str(i)[j])
    ls1=list(reversed(ls))
    a+=int(''.join(ls)+''.join(ls1))%p


print(int(a%p))