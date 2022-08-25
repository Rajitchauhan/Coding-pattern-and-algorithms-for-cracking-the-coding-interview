""" there are three type of edit [insert , replace , remove] can be performed in string
EX :: pale , ple -> True [remove operation performed]
      pale , pales -> True [insert operation performed]
      pales , pale -> True [insert operation performed]
      pale , bale -> True [replace operation performed]
      pale , bae -> False [remove and replace operations performed]
NOTE: we can perform only one operation at a time

 """

def one_away(str1 , str2):
    st1  , st2 = len(str1) , len(str2)
    res = None
    count = 0
    # if differnce of two string is more then one then simpl return False
    if st1 - st2 >= 2 or st2 - st1 >= 2:
        res = False
    # now check if word1 is less then word2
    elif (st1 < st2):
        count = 0
        i = 0
        # traverse till word1 BCZ word1 is less then word2
        while(i < st1):
            # both elements of word1 and word2 is equal then inceament i for checking next elements of word
            #otherwise inceament  count and check if it is more then one (means operation are performed more than one)
            # return False
            if str1[i] == str2[i]:
                i += 1
            else:
                count += 1
                if count > 1:
                    res = False
        res = True


    elif (st1 == st2):
        for i in range(st1-1):
            if str1[i] != str2[i]:
                count += 1
                if count > 1:
                    res = False
        res = True

    else:
        i = 0
        count = 0
        while (i < st2):
            if str1[i] == str2[i]:
                i += 1
            else:
                count += 1
                if count > 1:
                    res = False
        res = True
    return  res


str1 , str2 = "paless" , "pales"
print(one_away(str1 , str2))
