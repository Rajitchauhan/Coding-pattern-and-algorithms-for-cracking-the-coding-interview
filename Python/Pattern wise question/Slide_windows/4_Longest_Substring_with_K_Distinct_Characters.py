"""
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
"""
#bruit force 
class Sliding_variable:
    def longest_subStr(self , k , S):
        mini = float("-inf")
        for i in range(len(S)):
            ump = {}
            for j in range(i , len(S)):
                ump[S[j]] = ump.get(S[j] , 0) + 1
                if(len(ump) > k):
                    break
                mini = max(mini ,  j-i+1)
                #if(len(ump) == k):
                #    mini = max(mini , j-i+1)


        return mini

class Sliding_variable1:
    def longest_subStr(self , k , S):
        start  , end = 0 , 0
        mp = {}
        mini = float('-inf')
        for end in range(len(S)):
            mp[S[end]] = mp.get(S[end] , 0) + 1
            while(len(mp) > k):
                mp[S[start]] = mp.get(S[start] , 0) - 1
                if(mp[S[start]] == 0):
                    del mp[S[start]]
                start += 1
            mini = max(mini , end - start + 1)
        return mini


if __name__ == "__main__":
    obj = Sliding_variable()
    res = obj.longest_subStr(2 ,  "araaci")
    print(f"longest size substring is {res}")
