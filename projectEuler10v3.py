#! python3

def main():

	minInt = 2
	maxInt = 2000000
	intList = list(range(minInt,maxInt))

	print(removeProducts(intList,minInt))


def removeProducts(inputList,x):
	
	copyInputList = list(inputList)
	for a in inputList:
		if a%x == 0:
			copyInputList.remove(a)
	return copyInputList

main()


