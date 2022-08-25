#multi line write a code

x = (1+2+3
     +5-1

)

print(x)

# use ' ; ' semi colon in python

a = 1; b = 2; c = 3

if True: print('semicolor'); a = a+5; print(a)

#assign multiple value in multiple variable

x , y , z = 12, 23 , 34

print(x , '\n' , y , '\n' , z)

# copy one value into multiple variables

i = j = k = 10,000,000
print(i ,  '\n', j ,'\n', k)


aa = bb = cc = "Rajit"

print(aa , "\n" , bb)

log = 10,000,000,000
print(log)



# tries o\p - (12, 23, 34)
ty = 12,23,34
print(ty)
print(type(ty))

# <class 'tuple'>


# formatting using format function

print(" value a is {} and b is {} and c is {}" .format(a, b, c))

# another way to formatting

print(f"this is another way : a is {a} and b is {b}  and c is {c}")

# using tuples , we can indexing also
print("i love {0} and {1}".format('Gori' , 'shiv'))

print("i love {} and {}".format('Gauri' , 'shiv'))

print("i love {0} and {0}".format('Gauri' , 'shiv'))

print("i love {1} and {1}".format('Gauri' , 'shiv'))

#  input user

name = input('plzz enter the name : ')

age = int(input('please enter your age : '))

print("hello : {} sir , your age is {}".format(name , age))
