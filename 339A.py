list = input().split('+')
for i in range(len(list))[::-1]:
    for j in range (i):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]

print("+".join(list))

