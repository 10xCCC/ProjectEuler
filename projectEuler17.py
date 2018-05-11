#! python3

DIGITS_BEFORE_TWENTY = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def main():

	hundred = 'hundred'
	one_thousand = 'onethousand'

	total_letter_count = 0
	for a in range(1,1001):
		print(a)
		if a > 999:
			total_letter_count += len(one_thousand)
			print(one_thousand)
		else:

			b = a // 100
		
			if b > 0:
				print(DIGITS_BEFORE_TWENTY[b], hundred,)
				total_letter_count += len(hundred) + len(DIGITS_BEFORE_TWENTY[b])
			c = a % 100
			if b > 0 and c > 0:
				print('and')
				total_letter_count += 3
			# print(c)
			if c > 0:

				total_letter_count += non_hundred_letter_count(c) 



	print(total_letter_count)

def non_hundred_letter_count(n):
	''' assumes n is between 0 and 99 inclusive'''
	temp_letter_count = 0
	if n < 20:
		temp_letter_count += len(DIGITS_BEFORE_TWENTY[n])
		print(DIGITS_BEFORE_TWENTY[n])

	if n >= 20:
		a = n // 10
		b = n % 10
		print(TENS[a], DIGITS_BEFORE_TWENTY[b])
		temp_letter_count += len(TENS[a])
		temp_letter_count += len(DIGITS_BEFORE_TWENTY[b])


	return temp_letter_count



main()
