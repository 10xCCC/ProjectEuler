#finished 12/31/17

def main():
	
	palindromeProductList = []

	for x in range (100,999):
		for y in range(100,999):
			a = x*y
			if isPalindrome(a) == True:
				palindromeProductList.append(a)

	print max(palindromeProductList)


def isPalindrome(x):
	#returns a boolean that says whether the number is a palindrome or not
	xString = str(x)
	#print xString
	xRevString = xString[::-1]
	#print xRevString
	confirmedPalindrome = (xString == xRevString)
	#print confirmedPalindrome
	return confirmedPalindrome


main()