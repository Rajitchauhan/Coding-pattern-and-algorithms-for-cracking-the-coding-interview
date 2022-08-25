#check if a string contains all unique characters
"""
#method
def check_all_ele_unique(str):
    str = str.replace(" ","")
    str = str.lower()

    if len(str) > 256:
        return False
    else:
        return len(set(str)) == len(str)

print(check_all_ele_unique("Rajit chauhan"))


#Using Counter
from collections import Counter
def check_all_ele_unique(str):
    str = str.replace(" ","")
    str = str.lower()
    cn = Counter(str)

    if len(str) > 256:
        return False
    else:
        return len(str)  == len(cn)
print(check_all_ele_unique("Rajit"))


#using neasted loop O(n2)
def check_all_ele_unique(str):
    str = str.replace(" ","")
    str = str.lower()

    if len(str) > 256:
        return False
    else:
        for i in range(len(str)):
            for j in range(i + 1 , len(str)):
                if str[i] == str[j]:
                    return False

    return True
print(check_all_ele_unique("Rajit cchahan"))

"""
def uniqueCharacters(str):

    # Assuming string can have characters
    # a-z this has 32 bits set to 0
    checker = 0

    for i in range(len(str)):
        bitAtIndex = ord(str[i]) - ord('a')

        # If that bit is already set in
        # checker, return False
        if ((bitAtIndex) > 0):
            if ((checker & ((1 << bitAtIndex))) > 0):
                return False

            # Otherwise update and continue by
            # setting that bit in the checker
            checker = checker | (1 << bitAtIndex)

    # No duplicates encountered, return True
    return True


print(uniqueCharacters("Rajit"))

