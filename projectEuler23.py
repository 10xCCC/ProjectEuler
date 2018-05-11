#! python3

# calculate total of all numbers that cannot be expressed as the sum of two abundant numbers

def divisorSum(n):
	''' returns total of all divisors'''
	a = n
	b = n - 1
	divisor_sum = 0
	while b > 0:
		if a % b == 0:
			divisor_sum += b
		b -= 1

	return(divisor_sum)


max = 20161

abundant_list = []
abundant_dict = {}

non_abundant_sum = 0

x = list(range(1, max + 1))

print(x)

for a in range(1,10):
		abundant_dict[a].add(a)

print(abundant_dict)


