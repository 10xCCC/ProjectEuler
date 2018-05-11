#! python3

# longest collatz sequence starting under 1 million


def main():

	x = 1
	max_collatz_count = 1
	max_collatz_number = 1

	while x < 1000000:
		print(x)
		temp_collatz_count = collatz_counter(x)

		if temp_collatz_count > max_collatz_count:
			max_collatz_count = temp_collatz_count
			max_collatz_number = x

		x += 1

	print(max_collatz_number)







def collatz_counter(n):
	'''
	input: positive integer
	output: count of series to get back to 1
	'''

	counter = 1

	while n > 1:
	
		if n % 2 == 0:
			n = n/2
			counter += 1
		else:
			n = 3*n + 1
			counter += 1


	return counter





main()