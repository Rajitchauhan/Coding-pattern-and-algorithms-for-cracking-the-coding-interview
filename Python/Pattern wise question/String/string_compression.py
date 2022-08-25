"""
String compression :
input :  aabbcccc
output : {'a' , '2' , 'b' ,'2 ', 'c' , '4'} return length == 6

input : ["a"]
output : a return  length == 1

input :: abbbbbbbbbbb
output : {'a' , "b" , '1' , '2'} return length == 4
"""
def compress(string):
    index = 0
    compressed = ""
    len_str = len(string)

    while index != len_str:
        count = 1
        # traverse the whole string using index
        #and string[index] is equal to next string index string[index+1]
        # then inceament count  , index
        while (index < len_str-1) and (string[index] == string[index+1]):
            count = count + 1
            index = index + 1
        #if index is equal to 1 then simply add a string into empty variable compressed
        if count == 1:
            compressed += str(string[index])
        # other wise add string with their counting numbers
        else:
            compressed += str(string[index]) + str(count)

        index = index + 1 # for traverse whole string

    return list(compressed) , len(compressed)


string = "abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
print(compress(string))
