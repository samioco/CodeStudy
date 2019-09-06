#BubbleSort.py

'''
Notes:
Last i elements are already in place
i.e. i=1 loop swapped the last pair of elements. 
Worst case i loop scenario: largest item in first index, moved the back via first i iteration
Worst case j loop scenario: smallest item in last index, requiest j loops to swap to front
'''

def print_main_menu():
	print("")
	print("Bubble Sort Algorithm:")
	print("From head of list, use nested loops to swap adjacent elements if they are out of order.")
	print("Time (Worst Case scenario fully reversed list): O(n*n)")
	print("Time (Best Case sceneario already sorted list): O(n)")
	print("")
	print("(1) Verbose Mode")
	print("(2) Brief Mode")
	print("(Q) Quit")


def main_menu():	
	while True:
		mylist = [8,7,1,9,2,5,6,0,3,4]
		try:
			print_main_menu()
			choice = str(input("Enter choice> "))
		except ValueError:
			print("Invalid input: ValueError.")
			continue
		if (choice != '1') and (choice!= '2') and (choice.upper()!='Q'):
			print("Invalid input: Not a valid menu item.")
			continue
		elif choice=='1':
			print(f"Option {choice} chosen. Verbose mode.")
			sorted_list = bubbleSort(mylist,1)
		elif choice=='2':
			print(f"Option {choice} chosen. Brief mode.")
			sorted_list = bubbleSort(mylist,0)
		elif choice.upper()=='Q':
			print("Goodbye!")
			break


def bubbleSort(mylist,mode):
	print("Test List:",mylist)
	for i in range(len(mylist)):
		swap_occurred = False
		#Last i elements are already in order
		#j loop up to len(mylist) - i - 1
		#-1 because we need to know that j+1 exists
		for j in range(0,len(mylist) - i - 1):
			#Swap if current (j) is greater than next (j+1)
			if mylist[j]>mylist[j+1]:
				if mode==1: print(f"i:{i} j:{j}, Swapping mylist[{j}]:{mylist[j]} and mylist[{j+1}]:{mylist[j+1]}")
				mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
				swap_occurred = True
			#if mode==1: print(f"Semi-sorted List: i:{i} j:{j} mylist[{j}]:{mylist[j]} mylist[{j+1}]:{mylist[j+1]}, mylist:{mylist}")
			if mode==1: print(f"i:{i} j:{j}, Semi-sorted List: {mylist}")

		#if a swap doesn't occur during entire j loop, then list is sorted!
		if swap_occurred == False:
			break
	print("Final Sorted List:",mylist)
	return mylist
#function test

#MAIN
main_menu()

