#MergeSort

def print_main_menu():
	print("(1) MergeSort: RuneStone Academy (single method)")
	print("(2) MergeSort: Amir Ziai (triple method)")
	print("(3) MergeSort: My Single Method approach")

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


def mergeLists(lefthalf,righthalf):
	merged_list = []

	#Merging/Sorting of lefthalf and righthalf
	i=0 #lefthalf index
	j=0 #righthalf index
	k=0 #merged_list index

	print("MERGING Left:",lefthalf,", Right:", righthalf)
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


	print("Returning List ",merged_list)
	return merged_list



def sortList(input_list):
	
	#Split the list
	#splitList(alist)
	
	if len(input_list)<=1:
		print("Returning Single Item List:",input_list)
		return input_list
	else:
		mid = len(input_list)//2
		lefthalf=input_list[:mid]
		righthalf=input_list[mid:]

		#Recursively call self (mergeSort) on splits
		print("Splitting Left Half:",lefthalf)
		lefthalf_sorted=sortList(lefthalf)
		print("RECEIVED: Left Half:",lefthalf_sorted)

		print("Splitting Right Half:",righthalf)
		righthalf_sorted=sortList(righthalf)
		print("RECEIVED: Right Half:",righthalf_sorted)
		
		sorted_list = mergeLists(lefthalf_sorted,righthalf_sorted)
		#print("Received Sorted List:",sorted_list)
		return sorted_list





#MAIN
mylist = [54,26,93,17,77,31,44,55,20]
list1=[5,3,1,2]
print("Splitting:",mylist)
sorted_list = sortList(mylist)

print("Final Sorted List: ",sorted_list)

