#CollatzConjecture
def get_input():
	while True:
		try:
			n = int(input("Enter starting number (integer > 1)> "))
		except ValueError:
			print("Invalid input: ValueError.")
			continue
		if n <= 1:
			print("Please enter a positive integer greater than 1.")
		else: 
			print(f"Appropriate input detected: {n}.")
			print("Calculating Collatz Conjecture steps...")
			break
	return n

def collatz(n):
	steps=0
	print(f"Step: {steps}, n: {n}")
	while n != 1:
		steps += 1

		if n%2==0:
			n /= 2
		else:
			n = n*3 + 1

		print(f"Step: {steps}, n: {n}")
	return steps
	

steps = collatz(get_input())
print("")
print(f"Reached 1 in {steps} steps!")
