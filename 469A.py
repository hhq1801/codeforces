n=int(input())
ls=input().split()
ls2=input().split()
def lint(list):
    list=[int(i) for i in list]
    del list[0]
    return list
ls=lint(ls)
ls2=lint(ls2)
lss=set(ls+ls2)
if len(lss)==n:
    print('I become the guy.')
else:print('Oh, my keyboard!')