#easy 重点在于怎么去掉字符串中的字符，利用index算出第一次出现的地方
s=input()
b=False
if 'AB' in s:
    n=s.index('AB')
    if n==0:
        k=s[(n+2):]
    elif n==len(s)-1:
        k=s[:n-1]
    else:
        k=s[0:n-1]+s[(n+2):]
    if "BA" in k:
        b=True
if b== False:
    if 'BA' in s:
        n = s.index('BA')
        if n == 0:
            k = s[(n + 2):]
        elif n == len(s) - 1:
            k = s[:n - 1]
        else:
            k = s[0:n - 1] + s[(n + 2):]
        if "AB" in k:
            b = True
if b==True:
    print("YES")
else:print("NO")


