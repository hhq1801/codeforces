n = int(input())
list = input().split()
list = [int(i) for i in list]
list1=[]
list2=[]
count = 0
for i in list:
    if i%2==0 :
        count +=1
        list1.append(list.index(i)+1)
    else:
        list2.append(list.index(i)+1)
if count ==1:
    print(list1[0])
else:
    print(list2[0])