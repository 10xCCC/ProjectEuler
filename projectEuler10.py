#! python3


def main():

	maxInt = 20
	intList = list(range(2,maxInt))
	copyIntList = list(intList)

	x = 0


	while x < len(copyIntList):
		


	print(scrubByDivisors(intList,intList[x]))


def scrubByDivisors(inputList,divisor):

	copyInputList = list(inputList)

	for a in inputList:
		if a%divisor == 0:
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





