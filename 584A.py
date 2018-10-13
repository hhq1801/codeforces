n,t=input().split()
n=int(n)
t=int(t)
if int('1'+(n-1)*'0')%t==0:
    print ('1'+(n-1)*'0')
else:
    a = (int('1'+(n-1)*'0')//t+1)*t
    if len(str(a))==n:
        print(a)
    else:
        print(-1)