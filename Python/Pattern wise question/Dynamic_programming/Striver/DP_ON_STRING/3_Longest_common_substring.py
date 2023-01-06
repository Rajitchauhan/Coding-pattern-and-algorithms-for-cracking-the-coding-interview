"""

Problem Statement
Detailed explanation ( Input/output format, Notes, Constraints, Images )
Sample Input 1:
2
abcjklp acjkp
wasdijkl wsdjkl
Sample Output 1:
3
3
Explanation For Sample Output 1:
In test case 1, the longest common substring is "cjk" of length 3.

In test case 2, the longest common substring is "jkl" of length 3.
Sample Input 2:
2
abcy acby
tyfg cvbnuty
Sample Output 2:
1
2


"""

def lcs(str1, str2):
    # Write your code here.
    m = len(str1)
    n = len(str2)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    maxi = 0
    for i in range(1 , m+1):
        for j in range(1 , n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                maxi = max(maxi , dp[i][j])
            else:
                dp[i][j] = 0
    return maxi
