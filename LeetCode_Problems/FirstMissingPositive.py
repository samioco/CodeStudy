#2. Find smallest missing positive integer not in the list
#[1,2,0] -> 3

def firstMissingPositive(mylist):
    mylist.sort()
    print("Received list: ",mylist)
    print("Removing negatives...")
    for item in mylist:
        if item<1:
            mylist.remove(item)
            print("Removed: ",item,", mylist: ",mylist)
    print("Cleaned list: ",mylist)

    i=1
    while len(mylist)>0:
        print("Testing: ",i)
        if i in mylist:
            print("Removing: ",i)
            mylist.remove(i)
            print("Mylist: ",mylist)
            i+=1
        else:
            print(i," not in list!")
            break
    print("Returning: ",i)
    return i

#list1 = [-5,1,2,0]
#list1 = [3,4,-1,1]
list1 = [7,8,9,11,12]
result = firstMissingPositive(list1)
print(result)
