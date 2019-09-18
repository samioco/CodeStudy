
#SortArrayByParity.py

#1. sort arrow in odds and evens
#[3,1,2,4] -> [2,4,3,1]
#evens first

def split_list(mylist):
    print("Received mylist: ",mylist)
    evenlist=[]
    oddlist=[]
    for item in mylist:
        print("Scanning item: ",item)
        if item % 2 == 0:
            print("Even item detected. Appending to evenlist: ",evenlist)
            evenlist.append(item)
        else:
            print("Odd item detected. Appending to oddlist: ",oddlist)
            oddlist.append(item)
    print("Done splitting list.")
    print("Evenlist: ", evenlist)
    print("Oddlist: ", oddlist)
    return evenlist, oddlist

def merge_lists(evenlist, oddlist):
    merged_list = []
    even_i=0
    odd_i=0
    while even_i < len(evenlist)-1:
        while odd_i < len(oddlist)-1:
            print("Comparing ",evenlist[even_i]," and ",oddlist[odd_i])
            if int(evenlist[even_i]) < int(oddlist[odd_i]):
                print("Appending ",evenlist[even_i])
                merged_list.append(evenlist[even_i])
                even_i += 1
            else: 
                print("Appending ",oddlist[odd_i])
                merged_list.append(oddlist[odd_i])
                odd_i += 1
            print("Merged list: ",merged_list)
            print("even_i: ",even_i,", odd_i: ",odd_i)
            continue
                
    return merged_list


mylist=[3,1,2,4]
#mylist.sort()
evenlist = []
oddlist = []
evenlist, oddlist = split_list(mylist)
print("")
print("Global lists:")
print("Even list: ", evenlist)
print("Odd list: ", oddlist)

print("")
sorted_merged_list=[]
#sorted_merged_list = merge_lists(evenlist,oddlist)
#print("Merged list: ", sorted_merged_list)

for item in evenlist:
    sorted_merged_list.append(item)
for item in oddlist:
    sorted_merged_list.append(item)


print(sorted_merged_list)