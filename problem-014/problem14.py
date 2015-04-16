# Project Euler
# Problem 14

results = {}

def checkStartingNumbers(start, end):
	for x in xrange(start, end):
		collatzSequence(x)

def collatzSequence(start):
	keepChecking = True
	n = start
	count = 0
	while keepChecking:	
		if n == 1:
			results[start] = count
			keepChecking = False
		elif (n % 2) == 0:
			n = n / 2
			count += 1
		else:
			n = 3*n + 1
			count += 1

checkStartingNumbers(1, 1000000)
result = max(results, key=results.get)
print result