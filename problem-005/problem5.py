# Project Euler
# Problem 5

def evenlyDivideNumWithRange(n,x,y):
    for a in range(x,y+1):
        if (n % a != 0):
            return False
    return True

def smallestSatisfyingNum(lower, upper):
    found = False
    n = upper

    while found == False:
        print "Checking:",n
        if evenlyDivideNumWithRange(n,lower,upper):
            return n
            found = True
        else:
            n += upper

print smallestSatisfyingNum(1, 20)
