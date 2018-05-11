#! python3

non_leap_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year =     [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_week = ['sun', 'mon', 'tues', 'weds', 'thurs', 'fri', 'sat']
# days since 30 Dec 1990, previous Sunday
days_since = 2
sundays_on_first = 0


for a in range(1901, 2001):
	# for each year - first, assign list of monthly date quantities
	# then increment through list and check if first is Sunday
	# if so, increment Sunday quantities
	monthly_quantities = []
	
	if a % 4 != 0:
		monthly_quantities = non_leap_year.copy()
		# print("non leap", a, monthly_quantities)
	elif a % 4 == 0:
		monthly_quantities = leap_year.copy()
		# print("leap", a, monthly_quantities)
	
	for b in monthly_quantities:
		# print(monthly_quantities[b])
		days_since += b
		if days_since % 7 == 0:
			sundays_on_first += 1
			# print("year", a)

print(sundays_on_first)
