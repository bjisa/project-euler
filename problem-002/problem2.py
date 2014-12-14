# Project Euler
# Problem 2

evenTermCount = 0
evenTermSum = 0

fibNumbers = [0]

def fibonacci():
    global evenTermCount
    global evenTermSum
    global fibNumbers
    fibTerm = -1
    x = 0

    while fibTerm < 4000000:
        if x == 0:
            fibTerm = 0
        elif x == 1:
            fibTerm = 1
        elif x > 1:
            fibTerm = fibNumbers[x-1] + fibNumbers[x-2]

        fibNumbers.insert(x,fibTerm)

        if fibTerm % 2 == 0:
            evenTermCount += 1
            evenTermSum += fibTerm
        x += 1

fibonacci()
print evenTermSum
