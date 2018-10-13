n = int(input())
ls1 = input().split()
m = input()
ls2 = input().split()
ls1 = [int(i) for i in ls1]
ls2 = [int(i) for i in ls2]
for i in ls2:
    for j in range(n):
        if i <= ls1[j]:
            print(j + 1)
            break
        else:i=i-ls1[j]
