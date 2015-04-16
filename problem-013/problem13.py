# Project Euler
# Problem 13

result = []
numbers = []

def loadLines():
    with open('input.txt') as input:
        lines = input.readlines()
    for line in lines:
        numbers.append(line)

def numbersSum():
    sum = 0
    for number in numbers:
        sum += int(number)
    return sum

loadLines()

result = str(numbersSum())
print result[:10]