#! python3

def main():
	
	'''
	input: balance, annualInterestRate, monthlyPaymentRate
	output: balance after one year

	'''
	balance = 42
	annualInterestRate = 0.2
	monthlyPaymentRate = 0.04

	# test answer: Remaining balance: 31.38

	monthlyInterestRate = annualInterestRate/12

	for x in range(0,12)
		unpaidBalance = balance - balance*monthlyPaymentRate
		interestCharge = unpaidBalance*monthlyInterestRate
		balance = unpaidBalance + interestCharge
		print balance

main()