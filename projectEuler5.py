#started 12/31/17

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# first step - created function to check for any Non Divisors. Tested it with given numbers
# doing a while loop with that would have taken too long

# cancelled the While loop. solved it using some number theory. actual answer was 232792560

def main():

	testSmallestNumber = 2521
	totalDivisors = 20

	areNonDivisors = True

	while areNonDivisors == True:
		areNonDivisors = checkForAnyNonDivisors(testSmallestNumber,totalDivisors)
		testSmallestNumber += 1
		print testSmallestNumber

	print testSmallestNumber

def checkForAnyNonDivisors(x,y):
	#returns True if any nonDivisors in intSmallNumber
	# x is small number
	# total divisors is y
	for a in range(1, y+1):
		b = x % a
		if b != 0:
			return True
	return False


main()
