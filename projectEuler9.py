#! python3

def main():
	'''
	A pythagorean triplet is a set of three natural numbers a<b<c for which a^2+b^2=c^2
	There exists exactly one Pythagorean triplet for which a+b+c = 1000
	Find the product a*b*c
	
	coding history:
	started out initializing variables a b c as 1 2 3, but that was pointless
	used for loop instead
	this code printed out the correct triple (200,375,425) but the wrong product
	bug: I typed print(z*y+x). fixed.
	'''

	for x in range(3,999):
		for y in range(2,x):
			for z in range(1,y):

				if z*z+y*y == x*x:
					print(z,y,x)
					if z+y+x == 1000:
						print(z*y*x)
						return z















main()
