"""

You are given a string s and an integer k. You can choose any character of the string and change
 it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.




Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start , end = 0 , 0
        ump = {}
        maxFreq = 0
        mini = 0
        for end in range(len(s)):
            ump[s[end]] = ump.get(s[end] , 0) + 1
            maxFreq = max(maxFreq , ump[s[end]])

            if((end - start + 1) - maxFreq) > k:
                ump[s[start]] = ump.get(s[start] , 0) - 1
                start += 1
            mini = max(mini , end - start + 1)
        return mini











if __name__ == "__main__":
    obj = Solution()
    res = obj.characterReplacement("ABAB" , 2)
    print(f"longest_subStr is {res}")
