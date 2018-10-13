#In this task we need to maximize the sum of numbers that we took. Let precalc array cnt. cnt[x] — number of integers x in array a. Now we can easily calculate the DP:
#f(i) = max(f(i - 1), f(i - 2) + cnt[i]·i), 2 ≤ i ≤ n;
#f(1) = cnt[1];
#f(0) = 0;
#The answer is f(n).
#Asymptotics — O(n).
n=int(input())
ls1=[int(i) for i in input().split()]
ls2=list(set(ls1))
ls2.sort()
dict={}
for i in range(max(ls2)+3):
    dict[i]=0

for j in ls1:
    dict[j]+=1
    
if max(ls2) == 1:
    print(dict[i]*i)
f0=0
f1=dict[1]
for i in range(2,max(ls2)+1,2):
    #f2=max(f0+dict[2]*2,f1)
    #f3=max(f2,f1+dict[3]*3)
    f0=max(f0+dict[i]*i,f1)
    f1=max(f0,f1+dict[i+1]*(i+1))

print(max(f1,f0))