n=int(input())
line=list(map(int, input().split()))
for m in range(len(line))[::-1]:
    for i in range(m):
        if line[i]> line[i+1]:
            line[i], line[i + 1] = line[i + 1], line[i]
line=[str(i) for i in line]
print(' '.join(line))