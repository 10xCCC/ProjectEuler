#! python3

def main():

	f = open("pe13hundred50digitnumbers.txt","r")

	digits_list = []
	for line in f:
		line = line.strip('\n')
		digits_list.append(line)


	print(digits_list)

	y = 0
	for x in digits_list:
		x = int(x)
		y += x

	print(y)




main()