"""
PS : print n numbers.
"""
#without loops
def print_numbers(n):
    #base condtion
    if n==1:
        return 1
    print_numbers(n-1)
    print(n)

print(1)
print_numbers(10)
