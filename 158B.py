import math
n = int(input())
list = input().split()
list = [int(i) for i in list]
m1 = 0
m2 = 0
m3 = 0
m4 = 0
for i in list:
    if i == 4:
        m4 += 1
    if i ==3:
        m3 += 1
    if i ==2:
        m2 += 1
    if i ==1 :
        m1 += 1
count = m4 + m3
if m3>=m1:
    m1 = 0
else:
    m1 -= m3
if m2 %2 ==0:
    count += m2/2 + math.ceil((m1)/4)
else:
    count += m2//2
    m2 =1
    if m1 <= 2:
        count +=1
    else:
        count += 1 + math.ceil((m1-2)/4)


print(int(count))