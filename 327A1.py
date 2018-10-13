
n = int(input())
list = input().split()
list = [int(i) for i in list]
ls = []

for i in list:
    if i == 1:
        ls.append(-1)
    else:
        ls.append(1)
thisSum = 0
maxSum = 0
for i in ls:
    thisSum += i
    if thisSum > maxSum:
        maxSum = thisSum
    elif thisSum < 0:
        thisSum = 0
if maxSum == 0:
    print(maxSum + sum(list) - 1)
else:
    print(maxSum + sum(list))
