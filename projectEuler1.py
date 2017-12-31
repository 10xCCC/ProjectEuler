#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.
#note: time to solve approx 10 mins, 12/31/17

def program():
	y = 0
	for x in range(1,1000):
		if x%3 == 0:
			y = y + x
			print y		
		elif x%5 == 0:
			y = y + x
			print y

program()



