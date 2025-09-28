def countNumber(myList, x):
    count = 0
    for element in myList:
        if element == x:
            count += 1
    return count