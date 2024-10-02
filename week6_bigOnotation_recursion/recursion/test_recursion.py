# def print_hi(name):
#     print("hi:", name)
#     print_hi("andy")

# print_hi("luke")

# only use recursion when the problem you're trying to solve is recursive by nature

lst = [3, 1, 4, 1, 5, 9, 2, 6]

# for i in lst:
#     print(i)

#print numbers in list using recursion

def print_number(lst, index, length):
    if index == length:
        return
    else:
        print(lst[index])
        print_number(lst, index + 1, length)


print_number(lst, 0, len(lst))