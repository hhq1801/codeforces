n=int(input())
dict={}
for i in range(n):
    new=input()
    if new in dict:
        print(new+str(dict[new]))
        dict[new]+=1
    else:
        dict[new]=1
        print("OK")
