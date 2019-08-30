#MergeSort

def print_main_menu():
	print("(1) MergeSort: RuneStone Academy (single method)")
	print("(2) MergeSort: Amir Ziai (triple method)")

def main_menu():
	while True:
		try:
			print_main_menu()
			choice = int(input("Enter choice (1 to 2)> "))
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
