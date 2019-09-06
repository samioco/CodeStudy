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


def bubbleSort(mylist):
	for i in range(len(mylist)):
		swap_occurred = False
		#Last i elements are already in order
		#j loop up to len(mylist) - i - 1
		#-1 because we need to know that j+1 exists
		for j in range(0,len(mylist) - i - 1):
			#Swap if current (j) is greater than next (j+1)
			if mylist[j]>mylist[j+1]:
				mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
				swap_occurred = True

		#if a swap doesn't occur during entire j loop, then list is sorted!
		if swap_occurred == False:
			break

#function test
mylist = [8,7,1,9,2,5,6,0,3,4]
print_main_menu()
print("Test List:",mylist)
bubbleSort(mylist)
print("Sorted List:",mylist)

