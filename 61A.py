str1=input()
str2=input()
ls=[]
for i in range(len(str1)):
    if str1[i]==str2[i]:
        ls.append('0')
    else:ls.append('1')
print(''.join(ls))