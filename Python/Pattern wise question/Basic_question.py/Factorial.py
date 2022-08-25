"""
5 = 5*4*3*2*1 = 120
"""
def factorial(n):
    fact = 1

    if n == 0:
        return fact
    else:
        while(0<n):
            fact *= n
            n -= 1
    return fact

print(factorial(6))
