w = input()
list1=[]
for i in range(len(w)):
    list1.append(w[i])
list2=list(set(list1))
if len(list2)%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')