"""
6 = 1*2*3 = 6 = 1+2+3
"""
def perfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

print(perfect(28))
