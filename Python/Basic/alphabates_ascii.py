
"""
Using ASCII values:
ASCII value of uppercase alphabets – 65 to 90.
ASCII value of lowercase alphabets – 97 to 122.

"""
# Python3 program to print alphabets

# Function to print the alphabet
# in lower case
def lowercaseAlphabets():

    # lowercase
    for c in range(97, 123):
        print(chr(c), end = " ");

    print("");

# Function to print the alphabet
# in upper case
def uppercaseAlphabets():

    # uppercase
    for c in range(65, 91):
        print(chr(c), end = " ");

    print("");

# Driver code
print("Uppercase Alphabets");
uppercaseAlphabets();

print("Lowercase Alphabets ");
lowercaseAlphabets();


"""
# This code is contributed by mits
Output:
Uppercase Alphabets
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Lowercase Alphabets
a b c d e f g h i j k l m n o p q r s t u v w x y z

"""
