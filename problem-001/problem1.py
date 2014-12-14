# Project Euler
# Problem 1

multiplesCounter = 0
multiplesSum = 0

def multiples(n):
    global multiplesCounter
    global multiplesSum
    for x in range(0,n):
        if multipleOf(x,3) or multipleOf(x,5) :
            multiplesCounter += 1
            multiplesSum += x

def multipleOf(n,x):
    if n % x == 0:
        return True
    else:
        return False

multiples(1000)
print multiplesSum
