"""
problem : given an array of strings , group anagram together
input  :: ['eat' , 'tea' , 'tan' ,'ate' , 'nat' , 'bat']
output :: [ ['ate' , 'eat' ,'tea'],
            ['nat' , 'tan'] ,
            ['bat']
                      ]

"""

def group_anagram(strs):
    dict = {}
    for word in strs:
        #sortedWord = "".join(sorted(word))
        sortedWord = str(sorted(word))

        if sortedWord not in dict:
            dict[sortedWord] = [word]
        else:
            dict[sortedWord].append(word)
    #print(dict)


    result = []
    for items in dict.values():
        result.append(items)
    return result

strs = ['eat' , 'tea' , 'tan' ,'ate' , 'nat' , 'bat']

print(group_anagram(strs))
