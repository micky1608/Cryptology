import math

def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

def fact_rho(N , f, init):
    x = init
    y = init
    d = 1
    while d==1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x-y) , N)
    if d==N:
        return 0 
    
    return d

def fact_rho_opt(N , f , x0 , cycle_size):
    i=0
    alpha = 1
    x = x0
    y = x0
    d = 1
    memory = [0 for x in range(cycle_size)]
    while d==1:
        i += 1
        x = f(x)
        y = f(f(y))
        memory[i%cycle_size] = abs(x-y)%N
        alpha = (alpha * (abs(x-y)))%N
        if i%cycle_size == 0:
            d = gcd(alpha , N)
            alpha = 1

    if d==N: 
        i = 0
        while i<cycle_size and d==N:
            d = gcd(memory[i] , N)
            i+=1
    
    return d

def poww(a , n):
    if n==0:
        return 1
    if n==1:
        return a
    if n%2 == 0 :
        return poww(a,n/2)*poww(a,n/2)
    else:
        return a*poww(a,(n-1)/2)*poww(a,(n-1)/2)      



N = 0x9431A636C300F2CD0868C4FFBB101163CD15188980761C2FAD6E534DB1DA13A7FB30E22F39D41277E6A5AC1C4157459E1E5001B4F807741C71B6AB8E64346A4B5454928B20D5B635B88EBEDD9AB1C791510B9B479B71C798431A07A04BAB01097EE71624F6AAEF82EE4D659822878F84232C96473D684012114F349A00D0DBCCB4197E6FC98879ED8670A3CD2AA696E6AAAC777C8B00AE48FC16BA4BFBD81FD4DA422047B44F7C7C517B39AEFE19BC80CECAF3160D827455495910C7C325DD34FA98D6B6744189A78C9DBC5F614677AA031DFE66A7A047C69CA5C0946379A440088528CA39115C9F1F3F3FE278ED9CFEFD559EB2C157B7860F0A779D1D9AF43B
init=2
p = fact_rho_opt(N , (lambda x:int(x**2+1)%N) , init , 10)

#p=152004274830911

print("p : ",p, " q : ", N//p)