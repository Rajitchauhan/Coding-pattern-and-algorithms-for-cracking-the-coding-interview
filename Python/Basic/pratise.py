"""
Write a program which prints all the divisors of a number.


n = int(input('enter your number'))

for i in range(1 , n+1):
    if n%i==0:
        print(f"dividor of number is {i}")


"""
"""
 program to check if input number is a prime number.




number = int(input("Enter any number: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
        break
    else:
        print(number, "is a prime number")


else:
    print(number, "is not a prime number")

"""


"""
Write a program to calculate factorial of a number.

"""

n = int(input("eenter the numbers"))

if n >= 0:
    fact = 1
    if n==0:
        print("factorial is 1")
    else:
        while n > 1:
            fact = fact* n
            n -= 1
        print(fact)
