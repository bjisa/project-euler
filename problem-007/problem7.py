# Project Euler
# Problem 7

def nextPrime(n):
    keepChecking = True

    while keepChecking:
        keepChecking = False
        n += 1
        for x in range(2,n):
            if (n % x == 0):
                keepChecking = True
    return n

def getPrime(n):
    primes = []
    currentPrime = 2
    primes.append(currentPrime)

    for x in range(2,n+1):
        print "Working on prime:",x
        currentPrime = nextPrime(currentPrime)
        primes.append(currentPrime)

    return primes

print getPrime(10001)[-1]
