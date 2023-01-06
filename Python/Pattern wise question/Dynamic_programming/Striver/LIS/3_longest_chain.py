
class Solution:
    def valid(self , s1 , s2):
        n1 , n2 = len(s1) , len(s2)
        if n1 != n2+1:
            return False
        i , j = 0 , 0
        while i < n1:
            if j < n2  and s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                i += 1
        if i == n1 and j == n2:
            return True
        else:
            return False



    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        #words.sort()
        words.sort(key = lambda x: len(x))
        dp = [1]*n
        maxi = -1
        for i in range(n):
            for j in range(i):
                if self.valid(words[i] , words[j]):
                    if dp[i] < 1 + dp[j]:
                        dp[i] = 1 + dp[j]
            if maxi < dp[i]:
                maxi = dp[i]
        return maxi
