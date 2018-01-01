#started 5:36pm 12/31/17
#ended 

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def main():
	

	# numberToFactor = 600851475143
	
	primeList = generateCompletePrimeList(numberToFactor)
	print primeList




def generateCompletePrimeList(x):
	# returns list with all primes between 2 and x

	primeList = []
	y = 2
	while y < x:
		a = checkPrime(y)
		if a == True:
			primeList.append(y)

		y = y+1
	return primeList

def checkPrime(x):
	for y in range(2,x/2):
		if x % y == 0:
			# print False

			return False
	else:
		# print True
		return True

main()




