
#easy one, code written correctly first try. only error was spaces instead of tabs, misalignment gave an error

def main():

	naturalMax = 100
	natMaxSumOfSquares = 0
	 

	for a in range(1,naturalMax +1):
	 	nextSquare = a*a
	 	natMaxSumOfSquares += nextSquare

	natMaxSum = 0

	for a in range(1, naturalMax+1):
		natMaxSum += a

	natMaxSquareOfSum = natMaxSum*natMaxSum

	print natMaxSquareOfSum - natMaxSumOfSquares






main()