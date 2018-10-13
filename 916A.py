x=int(input())
h,m=input().split()
if "7" in h or '7' in m:
    print(0)
else:
    h=int(h)
    m=int(m)
    c=h*60+m
    for i in range(1,100000):
        c=c-x
        if c<=0:
            c=24*60+c
        if '7' in str(c % 60) or '7' in str(c//60) :
            print(i)
            break


