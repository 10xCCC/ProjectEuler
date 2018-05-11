#! python3

dimension = 21
lineArray = [1]


for a in range(1, dimension):

	lineArray.append(1)
	tempArray = []
	if len(lineArray) > 2:
		for b in range(len(lineArray)-2):
			nextSum = lineArray[b] + lineArray[b+1]
			tempArray.append(nextSum)

	for c in range(len(tempArray)):
		lineArray[c + 1] = tempArray[c]

while len(lineArray) > 1:
	tempArray = []
	for d in range(len(lineArray)-1):
		nextSum = lineArray[d] + lineArray[d+1]
		tempArray.append(nextSum)

	lineArray = tempArray
print(lineArray)








# dimension = 20
# gridArray = np.zeros((dimension,dimension),dtype = np.int16)



# gridArray[dimension - 1, dimension -1] = 1

# max_reference = dimension - 1

# print(gridArray)

# while max_reference >= 0:

# 	i = max_reference
# 	j = max_reference - i

# 	iter_tuple = (i,j)
	
# 	while i >= 0:
# 		print(iter_tuple)
# 		i -= 1
# 		j += 1
# 		iter_tuple = (i,j)
		

# 	max_reference -= 1