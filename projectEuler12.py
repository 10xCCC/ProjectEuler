#! python3

import math

def main():

	triangle_generator = next_triangle_number()

	divisor_count = 0


	while divisor_count <= 500:
		x = next(triangle_generator)
		# print(x)
		temp_divisor_count = len(list(divisorGenerator(x)))
		if temp_divisor_count > divisor_count:
			divisor_count = temp_divisor_count

			print(x, divisor_count)

	print(x)
	print(divisor_count)	


def divisorGenerator(n):
	large_divisors = []
	for i in range(1, int(math.sqrt(n)+1)):
		if n % i == 0:
			yield i
			if i*i != n:
				large_divisors.append(n / i)
	for divisor in reversed(large_divisors):
		yield divisor



def next_triangle_number():

	x = 1
	triangle_number = 0

	while True:
		triangle_number = triangle_number + x
		x += 1
		yield triangle_number

main()