# Project Euler
# Problem 4

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def nDigitProducts(n):
    palindromes = []
    number1 = 10 ** (n-1)
    number2 = number1
    max = (10 ** n) - 1

    for x in range(number1, max + 1):
        for y in range(number2, max + 1):
            candidate = x*y
            if isPalindrome(candidate):
                palindromes.append(candidate)

    return palindromes

print max(nDigitProducts(3))
