#! python3


def main():

	maxInt = 100

	knownPrimes = []

	x = 2

	while x < maxInt:
#		if x%1000 == 0:
#			print(x)
		if x > 1000:
			if x%1000 == 0:
				print(x)

		for a in knownPrimes:

			if x%a == 0:
				x += 1
				break

		if checkIfPrime(x) == True:
			knownPrimes.append(x)
			x += 1


	print(knownPrimes)




def removeProducts(inputList,x):
	
	copyInputList = list(inputList)
	for a in inputList:
		if a%x == 0:
			copyInputList.remove(a)
	return copyInputList

def checkIfPrime(x):
	b = 2
	while b < ((x/2) + 1):
		if x % b == 0:
			return False
		b += 1

	return True


main()