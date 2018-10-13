k,n,w=input().split()
k=int(k)
n=int(n)
w=int(w)
m=(k+w*k)*w/2
if m > n:
    print(int(m-n))
else:
    print(0)