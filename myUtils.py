
def gcd(a,b):
    if b>a:
        c = a
        a = b
        b = c
    
    return a if b == 0 else gcd(b , a%b)