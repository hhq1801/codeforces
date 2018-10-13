n = int(input())
list = []
list1 = []
for i in range(n):
    list.append(input())
for i in list:
    if len(i) > 10:
        m = i[0] + str(len(i) - 2) + i[-1]
        print(m)
    else:
        print(i)
