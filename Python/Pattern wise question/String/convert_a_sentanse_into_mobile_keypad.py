def printSeq(str , input):
    n=len(input)
    output = ""
    for i in range(n):
        if input[i]==" ":
            output += 0
        else:
            position = ord(input[i]) - ord('A')
            output = output + str[position]
    return output

str = ["2", "22", "222",
       "3", "33", "333",
       "4", "44", "444",
       "5", "55", "555",
       "6", "66", "666",
       "7", "77", "777", "7777",
       "8", "88", "888",
       "9", "99", "999", "9999" ]

input="SHIV"
print(printSeq(str , input))
