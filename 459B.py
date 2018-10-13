n = int(input())
ls = input().split()
ls = [int(i) for i in ls]
a = max(ls) - min(ls)
b = ls.count(max(ls)) * ls.count(min(ls))
if a == 0: b = int((n*n-n)/2)
print(a, b)
