"""
ARTHIMATIC PRGRESSION
a , a+d , a+2d , ...,a+(n-1)d
d = common difference
ex - 1 + 4 + 7 + 10 + 13 +... + n
first term = a
Nth term = a+(n-1)d

sum of n term of AP = n/2(2a+(n-1)d)

"""
n = 5
a = 1
d = 3

summ = (n/2)*(2*a+(n-1)*d)
print(f'sum of {n} term of AP is :: {summ}')

"""
GEOMATRIC PROGRESSION

a , ar , ar^2 , ar^3 , ar^4,....,ar^n-1
ex- 1 + x + x^2 + x^3 + x^4 +...+ x^n
first term  = a
Nth term = ar^n-1

sum of nth term = (ar^n-1/r-1)
"""
x = 1
n = 2
a = 1
r = x

summ = a*(r**n-1)/r-1
print(f"sum of nth of GP is {summ}")
