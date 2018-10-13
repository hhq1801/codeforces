import re
print("YES"if re.search("h.*e.*l.*l.*o",input())else"NO")


#
s=iter(input())
print('YNEOS'[any(c not in s for c in 'hello')::2])

#
a = input()
h = 0
e = 0
l = 0
o = 0
b = a.count("")
b = b - 1
for i in range(0, b):
    if a[i] == "h":
        h = h + 1
    if a[i] == "e" and h>=1:
        e = e + 1
    if a[i] == "l" and h>=1 and e>=1:
        l = l + 1
    if a[i] == "o" and h>=1 and e>=1 and l>=2:
        o = o + 1
if h >= 1 and e >= 1 and l >= 2 and o >= 1:
    print "YES"
else:
    print "NO"