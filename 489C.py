m,s=input().split()
m=int(m)
s=int(s)
ls=[]
if s==0 and m==1:
    print('0 0')
else:
    while s>9:
        ls.append(9)
        s=s-9
    else:
        ls.append(s)
    ls1=[str(i) for i in ls]
    a=''.join(ls1)

    if len(a)>m or a=='0':
        print('-1 -1')
    elif len(a)==m:
        print(a[::-1],a)
    else:
        b='1'+(m-len(a)-1)*'0'+str(int(a)-1)[::-1]
        a=a+(m-len(a))*'0'
        print(b,a)


