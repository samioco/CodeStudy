import math

def print_main_menu():
	print("(1) Calculate monthly payments")
	print("(2) Calculate payment term")

def main_menu():
	while True:
		try:
			print_main_menu()
			choice = int(input("Enter choice (1 or 2)> "))
		except ValueError:
			print("Invalid input: ValueError.")
			continue
		if (choice != 1) and (choice!= 2):
			print("Invalid input: Not a valid menu item.")
			continue
		else:
			print(f"Option {choice} chosen.")
			break
	return choice



#get_input param: main_menu choice
#if choice = 1, returns a tuple (principal, interest_rate (fixed APR), term (in years))
#if choice = 2, returns a tuple (principal, interest_rate (fixed APR), monthly_payment)
def get_input(choice):
	global principal
	global interest_rate
	global term
	global monthly_payment
	#Prompt for principle
	while True:
		try:
			principal = float(input("Principal amount> "))
		except ValueError:
			print("Invalid input: ValueError.")
			continue
		else: 
			print(f"Principal: ${principal}")
			break



	#Prompt for interest_rate
	while True:
		try:
			interest_rate = float(input("Interest Rate (%)> "))
		except ValueError:
			print("Invalid input: ValueError.")
			continue
		else:
			print("Annual interest rate: %.2f" % interest_rate)
			break


	#Prompt for desired term OR desired monthly_payment
	if choice == 1:
		while True:
			try:
				term = int(input("Payment term (years)> "))
			except ValueError:
				print("Invalid input: ValueError.")
				continue
			if term<1:
				print("Invalid term length.")
				continue
			else:
				print(f"Term: {term} years. {term*12} months.")
				break

		#return (principle,interest_rate,term)
		print("Principal: $%.2f" % principal)
		print("Interest rate: %.2f" % interest_rate)
		print("Term: %.2f years." % term)
		
	elif choice == 2:
		while True:
			try:
				monthly_payment = float(input("Desired monthly payment> "))
			except ValueError:
				print("Invalid input: ValueError.")
				continue
			if monthly_payment<1:
				print("Invalid payment amount.")
				continue
			else:
				print(f"Monthly payment: {monthly_payment}")
				break
		#return (principle, interest_rate, monthly_payment)
		print("Principal: $%.2f" % principal)
		print("Interest rate: %.2f" % interest_rate)
		print("Monthly payment: $%.2f" % monthly_payment)


def calculate_payment():
	p = float(principal)
	r = float(interest_rate/100/12)
	n = float(term*12)

	print(f"P: {p}, monthly_r: {r}, #months: {n}")

	monthly_payment = (r * p) / (1 - ((1+r)**(-n)))
	#m = (r / (1 - (1 + r)**(-n))) * p

	print(f"Monthly payment: {monthly_payment}")
	return monthly_payment

#calculate_term formula not working
#possible error in math logic
def calculate_term():
	p = float(principal)
	r = float(interest_rate/100/12)
	c = float(monthly_payment)
	N = (-1) * (math.log((1-(r*p/c)),(1+r)))

	print("Number of months to pay off mortgage: %.0f" % N)
	return N


def print_summary():
	#print("%10s %10s %20.4f" % ("Original Principal:", "$", principal))
	#print("%10s %30.2f %2s" % ("Anual Interest Rate:", interest_rate, "%"))
	#print("%10s %30.0f %10s" % ("Term (years):", term, "years"))
	print(" ")
	print("Mortgage Summary:")
	print("{0:<30s} {1:>3s} {2:>20,.2f}".format("Principal:","$", principal))
	print("{0:<30s} {1:>3s} {2:>20,.2f}".format("Interest Rate (APR):", " ", interest_rate))
	print("{0:<30s} {1:>3s} {2:>20,.0f} {3:10s}".format("Term (years):", " ", term, "years"))
	print("{0:<30s} {1:>3s} {2:>20,.0f} {3:10s}".format("Term (months):", " ", term*12, "months"))
	print("{0:<30s} {1:>3s} {2:>20,.2f}".format("Monthly Payment:", "$", monthly_payment))
	
	print(" ")
	print("{0:<30s} {1:>3s} {2:>20,.2f}".format("Total Principal Payments:","$", principal))
	print("{0:<30s} {1:>3s} {2:>20,.2f}".format("Total Interest Payments:", "$", (term*12*monthly_payment)-principal))
	print("{0:<30s} {1:>3s} {2:>20,.2f}".format("Total Payments:", "$", term*12*monthly_payment))


principal=0
interest_rate=0
term=0
monthly_payment=0
total_interest_payments=0
total_payments=0

print_summary()



choice = main_menu()
get_input(choice)

if choice == 1:
	monthly_payment=calculate_payment()

elif choice == 2:
	term=calculate_term()

print_summary()
