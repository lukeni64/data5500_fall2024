#### 
# Recursive Example 2
# Sum numbers iteratively

def sum_numbers(n):
    total = 0
    for i in range(1,n+1):
        total += i
        
    return total
    
print(sum_numbers(5))


def factorial_rec(n):
    #base case: when we get to 1, X /\
    if n == 1:
        return n
    if n == 0:
        return 1
    #logic add up n to n-1
    #make a recursive call to argument: n-1
    #return what comes back from our recursive call
    return n * factorial_rec(n-1)

print(factorial_rec(5))