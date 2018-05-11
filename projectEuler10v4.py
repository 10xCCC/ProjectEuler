#! python3

def main():


	maxInt = 2000000

	print(sum(primes_sieve1(maxInt)))



def primes_sieve1(limit):
	limitn = limit + 1
	primes = dict()
	for i in range(2, limitn): primes[i] = True

	for i in primes:
		factors = range(i, limitn, i)
		for f in factors[1:]:
			primes[f] = False

	return [i for i in primes if primes[i] == True]






















main()
