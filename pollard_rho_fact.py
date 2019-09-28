from myUtils import *

def fact_rho(N , f, iter):
    x = 2
    y = 2
    d = 1
    i = 0
    while d==1 and i < iter:
        x = f(x)%N
        y = f(f(y))%N
        d = gcd(abs(x-y) , N)%N
        i+=1
    if d==N:
        return 0,0   
    
    return d,int(N/d)



N = 8051
p,q = fact_rho(N , (lambda x:x**2+1) , 10)
print(N , " = " , p , "*" , q)