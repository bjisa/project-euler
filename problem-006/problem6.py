# Project Euler
# Problem 6

def sumOfSquares(n):
    sum = 0
    for x in range(0,n+1):
        sum += x*x
    return sum

def squareofSum(n):
    sum = 0
    for x in range(0,n+1):
        sum += x
    return sum*sum

print squareofSum(100) - sumOfSquares(100)
