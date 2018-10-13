import string
n = input()
count=n.count("7")+n.count('4')
a = str(count)
if a.count('4')+a.count('7') != len(a):
    print("NO")
else:
    print("YES")


