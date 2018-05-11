#! python3

#things I'll learn - how to read a text file
# this was probably easier when I did it in matlab


def main():

	f = open("pe11matrix.txt","r")
	
	matrixList = []
	for line in f:
		line = [int(s) for s in line.split(' ')]
		matrixList.append(line)
	
	maxProduct = 1

	# HORIZONTAL CALCS


	for row in range(20):
		x = matrixList[row]
		for z in range(0,len(x)-3):
			iterProduct = fourIntProduct(x[z:z+4])

			if iterProduct > maxProduct:
				maxProduct = iterProduct

	# print(maxProduct)

	# FLIP MATRIX

	mirrorMatrix = []

	for i in range(20):
		mirrorMatrix.append([])

	# print(mirrorMatrix)

	for origRow in range(20):
		for origColumn in range(20):
			x = matrixList[origRow]
			y = x[origColumn]
			mirrorMatrix[origColumn].append(y)

	# print(mirrorMatrix)


	# redo horizontal calcs on flipped matrix

	mirrorMaxProduct = 1

	for row in range(20):
		x = mirrorMatrix[row]

		for z in range(0,len(x)-3):
			iterProduct = fourIntProduct(x[z:z+4])

			if iterProduct > mirrorMaxProduct:
				mirrorMaxProduct = iterProduct
				# print(mirrorMaxProduct)

	print(maxProduct,mirrorMaxProduct)


	# finally, figure out diagonal calcs
	# use orig matrix - matrixList

	diagMaxProduct = 1

	for initRow in range(0,17):
		for initColumn in range(0,17):
			diagIterProduct = 1

			iterCount = 0

			while iterCount < 4:
				# print(initRow + iterCount, initColumn + iterCount)

				x = matrixList[initRow + iterCount]

				y = x[initColumn + iterCount]

				diagIterProduct *= y
				iterCount += 1


			if diagIterProduct > diagMaxProduct:
				diagMaxProduct = diagIterProduct

	print(diagMaxProduct)

	rev_diagMaxProduct = 1

	for initRow in range(19, 2, -1):

		for initColumn in range(16, -1, -1):

			rev_diagIterProduct = 1

			iterCount = 0

			while iterCount < 4:

				x = matrixList[initRow - iterCount]

				y = x[initColumn + iterCount]

				rev_diagIterProduct *= y
				iterCount += 1


			if rev_diagIterProduct > rev_diagMaxProduct:
				rev_diagMaxProduct = rev_diagIterProduct

	print(rev_diagMaxProduct)




	
def fourIntProduct(inputList):
	if len(inputList) != 4:
		return 0
	else:
		y = 1
		for x in inputList:
			y *= x
		return y




main()