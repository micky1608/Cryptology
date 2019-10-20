import numpy as np

N = int(1e7)

def getprime(N):
        is_prime = [True for x in range(N+1)]
        is_prime[0] = is_prime[1] = False


        for i in range(2,N+1):
                if is_prime[i] == True and i*i <= N:
                        for j in np.arange(i*i, N+1 , i):
                                is_prime[j] = False
        
        primes = []
        
        for i in range(N+1):
                if is_prime[i]==True:
                        primes.append(i)
        
        return primes
