s,n=map(int,input().split())
lsx=[]
lsy=[]
for i in range(n):
    a, b = map(int, input().split())
    lsx.append([a,b])
for m in range(len(lsx))[::-1]:
    for i in range(m):
        if lsx[i][0]  > lsx[i + 1][0] :
            lsx[i], lsx[i + 1] = lsx[i + 1], lsx[i]
for i in lsx:
    if i[0]<s:
        s+=i[1]
        n=n-1
    else:
        break
if n==0:
    print("YES")
else:print("NO")

