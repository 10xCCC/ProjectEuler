#! python3

def main():
	amicable_sum = 0

	amicable_number_list = []

	for a in range(1, 10000):
		x = divisorSum(a)
		
		if x == 0 or x == 1 or x == a:
			continue

		if a in amicable_number_list:

			continue

		y = divisorSum(x)
		

		if a == y:
			
			amicable_sum += a
			amicable_sum += x
			amicable_number_list.append(a)
			amicable_number_list.append(x)

	print(amicable_sum)



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
main()