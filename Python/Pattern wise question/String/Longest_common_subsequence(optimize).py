def lcs(str1  ,str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    return dp[m][n]

str1="ABCDGH"
str2="AEDFHR"
print(lcs(str1,str2))
