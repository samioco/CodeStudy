#4. Next lock combo
#"1450"  -> [2450, 0450, 1550, 1350, 1460, 1440, 1451, 1459]


def nextLockCombo(combo):
    print("Calculating neighboring combos...")
    
    #var declaration
    result=[]
    

    #convert combo to list of ints
    combo = list(combo)
    for i in range(len(combo)):
        combo[i] = int(combo[i])

        #depending on i (0-3), attach numbers up to current notch
        next_up_combo=''
        next_down_combo=''
        for j in range(i):
            next_up_combo += str(combo[j])
            next_down_combo += str(combo[j])
            print("next_up_combo: ",next_up_combo)
            print("next_down_combo: ",next_down_combo)
        
        #calculate next notch's next incremental #
        nextnum=combo[i]+1
        if nextnum>9:
            nextnum=0
        next_up_combo += str(nextnum)
        print("next_up_combo: ",next_up_combo)

        #calculate next notch's next decremental #
        nextnum=combo[i]-1
        if nextnum<0:
            nextnum=9
        next_down_combo += str(nextnum)
        print("next_down_combo: ",next_down_combo)

        #depending on i (0-3), attach numbers after current notch
        for j in range(i+1,len(combo)):
            next_up_combo += str(combo[j])
            next_down_combo += str(combo[j])
            print("next_up_combo: ",next_up_combo)
            print("next_down_combo: ",next_down_combo)
        
        #nextcombo now complete
        result.append(next_up_combo)
        result.append(next_down_combo)
        print("Results: ",result)

    return result



combo='1450'
print("Input combo: ",combo)

result = nextLockCombo(combo)
print("Result: ",result)

