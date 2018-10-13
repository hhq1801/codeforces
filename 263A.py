list1 = input().split()
list2 = input().split()
list3 = input().split()
list4 = input().split()
list5 = input().split()
ls=list1+list2+list3+list4+list5
a=ls.index('1')
tuple=(a-(a//5)*5,(a)//5)
print(abs(tuple[0]-2)+abs(tuple[1]-2))