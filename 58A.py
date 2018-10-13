n = input()
ls2=[]
count=0

for i in range(len(n)):
    if n[i] == "h":
        ls2.append(n[i])
        count = i
        break
for i in range(count+1,len(n)):
    if n[i] == "e":
        ls2.append(n[i])
        count = i
        break
for i in range(count+1,len(n)):
    if n[i] == "l":
        ls2.append(n[i])
        count = i
        break
for i in range(count+1,len(n)):
    if n[i] == "l":
        ls2.append(n[i])
        count = i
        break
for i in range(count+1,len(n)):
    if n[i] == "o":
        ls2.append(n[i])
        count = i
        break
if 'hello' in ''.join(ls2):
    print('YES')
else:
    print('NO')