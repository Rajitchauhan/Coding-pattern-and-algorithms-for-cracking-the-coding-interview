"""
2 power 2 = 4

base  , exponent = 3 , 4 = 3*3*3*3 =  81
"""
base = 3
exponent = 4
result = 1

while exponent != 0:
    result *= base
    exponent -= 1

print(result)
