# Project Euler
# Problem 3

def nextPrime(n):
    keepChecking = True

    while keepChecking:
        keepChecking = False
        n += 1
        for x in range(2,n):
            if (n % x == 0):
                keepChecking = True
    return n

def primeFactorization(n):
    factors = []
    count = 0
    divisor = 2;

    while n != 1:
        if (n % divisor == 0):
            factors.insert(count,divisor)
            n = n/divisor
            count += 1    
        else:
            divisor = nextPrime(divisor);

    return factors

print max(primeFactorization(600851475143))
