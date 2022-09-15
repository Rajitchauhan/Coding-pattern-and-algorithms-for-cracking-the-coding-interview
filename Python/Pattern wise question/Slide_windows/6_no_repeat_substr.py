"""

No-repeat Substring (hard)
We'll cover the following
Problem Statement #
Given a string, find the length of the longest substring
 which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".



"""

class Solution:
    def no_repeat_substr(self , S):
        beg = 0
        mini = float("-inf")
        ump = {}
        for last in range(len(S)):
            if(S[last] in ump):
                beg = max(beg , ump[S[last]] + 1)
            ump[S[last]] = last

            mini = max(mini , last - beg + 1)
        return mini

if __name__ == "__main__":
    obj = Solution()
    res = obj.no_repeat_substr("aabbb")
    print(f"longest_subStr is {res}")
