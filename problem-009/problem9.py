# Project Euler
# Problem 9

def findTriplet(n):
    for b in range(0,n+1):
        for a in range(0,b):
            c = (a ** 2 + b ** 2) ** (0.5)
            if ((a + b + c == n) and (c % 1 == 0)):
                return a*b*c

print findTriplet(1000)
