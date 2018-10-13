n=int(input())

def factorial(x): #阶乘
    y=1
    for i in range(1,x+1):
        y*=i
    return y
def Arrangement(x,y):
    return factorial(x)/factorial(x-y)
def Combination(x,y):
    return factorial(x)/(factorial(y)*factorial(x-y))
def PascalTriangle(a,b,n,x): #(a+b)^n 二项式定理 第x项
    


print(int(Combination(2*n-2,n-1)))