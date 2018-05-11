# code is slow but works. solved 1/2/18, took less than 15 mins

def main():

	numToCheck = 2
	primeCount = 0

	while primeCount < 10001:
		if checkIfPrime(numToCheck) == True:
			# print numToCheck

			primeCount += 1
			numToCheck += 1

			print primeCount
		else:
			numToCheck += 1

	numToCheck -= 1
	print numToCheck


def checkIfPrime(x):
	b = 2
	while b < x:
		if x % b == 0:
			return False
		b += 1

	return True

main()