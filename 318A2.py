a, b = input().split()
a = int(a)
b = int(b)
if a%2 == 0 :
    if b <= a/2:
        o = 2*b-1
    else:
        o= (b-a/2)*2
else:
    if b <= (a+1)/2:
        o=2*b-1
    else:
        o=(b-(a+1)/2)*2
print(int(o))