n = int(input())
count = 0
for i in range(n):
    str=input()
    if '++' in str:
        count +=1
    else:
        count -= 1

print(count)