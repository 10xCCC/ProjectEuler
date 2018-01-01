

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


#SOLVED 1/1/18

#challenge was finding right way to do it
#initial plan of calculating all possible primes, then searching through them, would have taken infinite time
#researched and used better recursive algo - find smallest possible prime factor
#code worked, but kept giving me error "/= is unsupported for NoneType"
#reason for error was that when I got to the final prime number
#my findSmallestPrimeFactor() would return NoneType if the input was prime
#changing the while loop to evaluate for a <= x, instead of a = x, 
#would return the input if it was prime, and added it to the list

def main():
	
	numberToFactor = 600851475143


	# print intMaxPrime

	#for z in range(100):
	#	print z, checkIfPrime(z)

	totalPrimeList = []

	while numberToFactor > 1:
		smallestPrimeFactor = findSmallestPrimeFactor(numberToFactor)
		print type(smallestPrimeFactor)
		print type(numberToFactor)
		print numberToFactor
		totalPrimeList.append(smallestPrimeFactor)
		numberToFactor /= smallestPrimeFactor
		print totalPrimeList

	 







def findSmallestPrimeFactor(x):
	a = 2
	while a <= x:
		if x % a == 0:
			return a
		else:
			a += 1


def generatePrimeList(x):
	primeList = []
	gplIncrement = 2
	while gplIncrement < x:
		#print gplIncrement
		primeTest = checkIfPrime(gplIncrement)
		#print primeTest
		if primeTest == True:
			primeList.append(gplIncrement)
			print gplIncrement
			#print primeList
		gplIncrement += 1

	return primeList

def checkIfPrime(x):
	b = 2
	while b < x:
		if x % b == 0:
			return False
		b += 1

	return True







main()

