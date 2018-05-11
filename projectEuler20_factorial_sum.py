#! python3

from math import factorial

x = factorial(100)
print(x)

total_digits = 0

while x > 0:
	y = x % 10
	total_digits += y
	x //= 10

print(total_digits)