#2. Find smallest missing positive integer not in the list
#[1,2,0] -> 3

def firstMissingPositive_2N(mylist):
    #mylist.sort()
    print("Received list: ",mylist)
    #print("Removing negatives, zero, and any number greater than length of list")
    for item in mylist:
        if item<1 or item>len(mylist)+1:
            mylist.remove(item)
            #print("Removed: ",item,", mylist: ",mylist)
    #print("Cleaned list: ",mylist)

    i=1
    while len(mylist)>0:
        #print("Testing: ",i)
        if i in mylist:
            #print("Removing: ",i)
            mylist.remove(i)
            #print("Mylist: ",mylist)
            i+=1
        else:
            #print(i," not in list!")
            break
    #print("Returning: ",i)
    return i

print("""
First Missing Positive Algorithm:
""")

list1 = [-5,1,2,0]
print("Input: ",list1)
result = firstMissingPositive_2N(list1)
print("Output firstMissingPositive_2N: ",result,"\n")

list1 = [3,4,-1,1]
print("Input: ",list1)
result = firstMissingPositive_2N(list1)
print("Output firstMissingPositive_2N: ",result,"\n")

list1 = [7,8,9,11,12]
print("Input: ",list1)
result = firstMissingPositive_2N(list1)
print("Output: firstMissingPositive_2N: ",result,"\n")
