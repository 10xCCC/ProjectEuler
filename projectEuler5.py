#started 6:25pm 12/31/17

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def main():

	x = 22

	
	boolList = [False]
	allTrue = all(x is True for x in boolList)


	while allTrue == False:
		y = range(1,21)
		boolList = []
		for a in y:
			
			if x%a != 0:
				boolList.append(False)
			else:
				boolList.append(True)
		allTrue = all(x is True for x in boolList)


	print x



main()
