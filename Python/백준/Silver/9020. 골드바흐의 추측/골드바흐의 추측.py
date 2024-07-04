import math

def isPrime(N):
    if N <= 1:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    N = int(input())
    for i in range(N//2, N) :
        if isPrime(i) and isPrime(N-i):
            print(N-i, i)
            break
    
