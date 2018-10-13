a, b = input().split()
a = int(a)
b = int(b) - 1
list = []
for i in range(1, a + 1, 2):
    list.append(i)
for i in range(2, a + 1, 2):
    list.append(i)
print(list[b])
# 如果a，b都特别大，就超时了
