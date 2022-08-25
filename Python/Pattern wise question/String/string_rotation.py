"""
You are given two strings as input. Write a function to check if one string is a rotation of the other string. An example of a rotation is


"CodingInterview", "erviewCodingInt"

You will also be given a function isSubstring that will return a boolean
that is True if one string is a substring of the other. You can only call this function once.

Input - "CodingInterview", "erviewCodingInt"
Output - True

Input - "Test", "est"
Output - False

Input - "waterbottel", "erbottelwat"
Output - True
"""
def isSubstring(s1, s2):
    if len(s1) >= len(s2):
        s2s2 = set(s2)
        res = set(s1).intersection(s2)
        if s2s2 == res:
            return True
    return False

def isRotaion(s1 , s2):
    if len(s1) != len(s2):
        return False
    elif (len(s1)== len(s2) and len(s1) > 0):
        s1s1 = str(s1) + str(s2)
        return isSubstring(s1s1 , s2)

    return False

#s1 , s2 = "waterbottel", "erbottelwat"

s1 , s2 = "Test", "est"

print(isRotaion(s1 , s2))
"""
solution :: s1 = xy = "waterbottel"
                 x = "wat"
                 y = "erbottel"
            s2 = yx = "erbottelwat"

"""
