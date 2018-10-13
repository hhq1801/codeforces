n=int(input())
str=input()
ls=[str[0]]
for i in range(1,len(str)):
    if str[i]!=str[i-1]:
        ls.append(str[i])
print (n-len(ls))