import string
list = []
list1=[]
str = input()
str = str.lower()

for i in range(len(str)):
    list.append(str[i])
for i in list:
    if i == 'a' or i == 'e'or i== 'i'or i == 'u' or i == "o" or i == 'y':
        m=1
    else:

        list1.append('.'+i)


print(''.join(list1))


