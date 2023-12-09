def nth_most_rate(intList, nth_term):
    newDict = {} # Creates empty dictionary to keep count of the integers
    for num in intList: # loops through inputted list
        if num in newDict:
            newDict[num] += 1 # adds to count if element already exists
        else:
            newDict[num] = 1 # initiates count for new element
    valueList = [value for value in newDict.values()] # put count in a list
    valueList.sort() # Sort the count from smallest to biggest
    if nth_term <= len(valueList):
        ref = valueList[nth_term - 1] # Gets the nth rarest count
        for key, val in newDict.items(): # loops through the dict to match nth rarest term to its value
            if ref == val:
                return key
    else:
        return "Nth term not found"
