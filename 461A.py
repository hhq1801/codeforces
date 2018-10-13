n=int(input())
if n ==1:
    print(input())
else:
    group=input().split()
    group=[int(i) for i in group]
    group.sort(reverse=True)
    if n>=3:
        score=n*(group[0]+group[1])
        for i in range(2,n):
            score+=(n+1-i)*group[i]
    elif n==2:
        score=2*sum(group)
    print(score)