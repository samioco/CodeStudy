#MergeSort

def print_main_menu():
	print("")
	print("Merge Sort Algorithm:")
	print("Divide and conquer. Divide input arrow into two halves. Recursively call itself on each half")
	print("until each half is split to a single item. Then merge each sorted half until the recursively")
	print("called functions are complete, resulting in a sorted list.")
	print("Time (Worst Case scenario fully reversed list): O(n*n)")
	print("Time (Best Case sceneario already sorted list): O(n)")
	print("")
	print("(1) Verbose Mode")
	print("(2) Brief Mode")
	print("(Q) Quit")

def main_menu():
	mylist = [54,26,93,17,77,31,44,55,20]
	list1=[5,3,1,2]
	
	while True:
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
			sorted_list = sortList(mylist,1)
			print("Final Sorted List: ",sorted_list)
		elif choice=='2':
			print(f"Option {choice} chosen. Brief mode.")
			sorted_list = sortList(mylist,0)
			print("Final Sorted List: ",sorted_list)
		elif choice.upper()=='Q':
			print("Goodbye!")
			break

	return choice


def mergeLists(lefthalf,righthalf,mode):
	merged_list = []

	#Merging/Sorting of lefthalf and righthalf
	i=0 #lefthalf index
	j=0 #righthalf index
	k=0 #merged_list index

	if mode==1: print("MERGING Left:",lefthalf,", Right:", righthalf)
	while i<len(lefthalf) and j<len(righthalf):
		if lefthalf[i] <= righthalf[j]:
			#merged_list[k] = lefthalf[i]
			merged_list.append(lefthalf[i])
			#alist[k]=lefthalf[i]
			i=i+1
		else:
			#merged_list[k] = righthalf[j]
			merged_list.append(righthalf[j])
			#alist[k]=righthalf[j]
			j=j+1
		k=k+1

	
	#Reached end of left/right list. Attaching remainders
	'''
	while i<len(lefthalf):
		#alist[k]=lefthalf[i]
		merged_list.append(lefthalf[i])
		#merged_list[k] = lefthalf[i]
		i+=1
		k+=1
	while j<len(righthalf):
		#alist[k]=righthalf[j]
		merged_list.append(righthalf[j])
		#merged_list[k] = righthalf[j]
		j+=1
		k+=1
	'''
	if i<len(lefthalf):
		merged_list += lefthalf[i:]
	elif j<len(righthalf):
		merged_list += righthalf[j:]


	if mode==1: print("Returning List ",merged_list)
	return merged_list



def sortList(input_list,mode):
	print("Splitting:",input_list)
	#Split the list
	#splitList(alist)
	
	if len(input_list)<=1:
		if mode==1: print("Returning Single Item List:",input_list)
		return input_list
	else:
		mid = len(input_list)//2
		lefthalf=input_list[:mid]
		righthalf=input_list[mid:]

		#Recursively call self (mergeSort) on splits
		if mode==1: print("Splitting Left Half:",lefthalf)
		lefthalf_sorted=sortList(lefthalf,mode)
		if mode==1: print("RECEIVED: Left Half:",lefthalf_sorted)

		if mode==1: print("Splitting Right Half:",righthalf)
		righthalf_sorted=sortList(righthalf,mode)
		if mode==1: print("RECEIVED: Right Half:",righthalf_sorted)
		
		sorted_list = mergeLists(lefthalf_sorted,righthalf_sorted,mode)
		#print("Received Sorted List:",sorted_list)
		return sorted_list




#MAIN
main_menu()


