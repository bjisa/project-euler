# Project Euler
# Problem 10

# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_description
def sieveOfEratosthenes(n):
    primes = []

    def enumerateMultiples(p):
        pCount = 2
        while (pCount * p) <= n:
            primes[pCount * p] = 0
            pCount += 1

    # 1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
    primes.append(0)
    primes.append(0)
    for x in range(2,n+2):
        primes.append(x)

    # 2. Initially, let p equal 2, the first prime number.
    p = 2

    while p <= n:
        # 3. Starting from p, enumerate its multiples by counting to n in increments of p, and mark them in the list
        # (these will be 2p, 3p, 4p, etc.; the p itself should not be marked).
        enumerateMultiples(p)

        # 4 Find the first number greater than p in the list that is not marked. If there was no such number, stop.
        # Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
        keepLooking = True
        while (p <= n and keepLooking):
            p += 1
            if primes[p] != 0:
                keepLooking = False

    # Remove zeros (marked numbers) from primes list
    primes = [x for x in primes if x != 0]
    del primes[-1]
    return primes

print sum(sieveOfEratosthenes(2000000))
