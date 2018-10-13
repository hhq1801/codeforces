n,m=input().split()
n=int(n)
m=int(m)
s=input()
str=[]
for i in range(len(s)):
    str.append(s[i])
for i in range(m):
    l,r,c1,c2=input().split()
    l=int(l)
    r=int(r)
    for i in range(r-l+1):
        if str[l-1]==c1:
            str[l-1]=c2
        l=l+1
print(''.join(str))

