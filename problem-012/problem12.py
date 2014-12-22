# Project Euler
# Problem 12

def triangleNumber(n):
    number = 0
    for x in range(0,n+1):
        number += x
    return number

def factorCount(n):
    factors = []
    for x in range(1, int(n**0.5) + 1):
        if (n % x == 0):
            factors.append(x)
            factors.append(n / x)
    return len(set(factors))

def triangleNumberWithDivisors(n):
    found = False
    currentNumber = 0

    while not found:
        currentNumber += 1
        candidate = triangleNumber(currentNumber)
        if factorCount(candidate) > n:
            found = True
            return candidate

print triangleNumberWithDivisors(500)
