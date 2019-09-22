#3. Max shared height of 3 stacks
#[4,2,1,1] 8
#[3,3,1,2] 9
#[5,1,2] 8

#-->6


def equalStacks(h1,h2,h3):
    
    

    while not sum(h1)==sum(h2)==sum(h3):
        h1sum=sum(h1)
        h2sum=sum(h2)
        h3sum=sum(h3)

        height=h1sum
        tallest='h1'
        if h2sum>h1sum: 
            height=h2sum
            tallest='h2'
        if h3sum>height: 
            height=h3sum
            tallest='h3'
        print("\nHighest: ",tallest,", ",height)

        print("\nLooping again...")
        if tallest=='h1':
            h1.pop()
        elif tallest=='h2':
            h2.pop()
        elif tallest=='h3':
            h3.pop()
        
        print("")
        print("New lists:")
        print("H1: ",h1, "Height: ",sum(h1))
        print("H2: ",h2, "Height: ",sum(h2))
        print("H3: ",h3, "Height: ",sum(h3))
        
    height = sum(h1)
    return height

h1=[4,2,1,1]
h2=[3,3,1,2]
h3=[5,1,2]
print("H1: ",h1, "Height: ",sum(h1))
print("H2: ",h2, "Height: ",sum(h2))
print("H3: ",h3, "Height: ",sum(h3))

result = equalStacks(h1,h2,h3)
print("Maximum shared height of all boxes: ",result)