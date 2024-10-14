lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 9]

#write an algorithm to sort all that data

#print the lst so it is now sorted
sortedlst = []
firstvalue = lst[0]
for i in lst:
    if lst[i] == firstvalue:
        pass
    elif lst[i] > lst[i-1]:
        lst[i-1] = lst[i]
    elif lst[i] < lst[i-1]:
        lst[i] = lst[i-1]
print(lst)