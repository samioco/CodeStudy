

def generate_fibonacci(n):
	a = 1
	b = 1
	for i in range(n):
		yield a
		a,b = b,a+b

def get_input():
	while True:
		try:
			num_fibs = int(input("Enter number of Fibonacci calculations (Integer)> "))
		except:
			print("Input Error!  Please enter a valid integer!")
			continue
		else:
			print(f"Thanks for inputting a valid integer: {num_fibs}")
			break
	return num_fibs

def print_fibonacci(fib_series):
	print(f"Generating Fibonacci's sequence to the {len(fib_series)}th position...")
	print(fib_series)


#MAIN
num_fibs = get_input()

fib_series = []
for num in generate_fibonacci(num_fibs):
	fib_series.append(num)

print_fibonacci(fib_series)

