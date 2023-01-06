"""
Alien Dictionary
Hard Accuracy: 47.81%        Submissions: 51K+               Points: 8
Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. Find the order of characters in the alien language.
Note: Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.

Example 1:
Input:
N = 5, K = 4
dict = {"baa","abcd","abca","cab","cad"}
Output:
1
Explanation:
Here order of characters is
'b', 'd', 'a', 'c' Note that words are sorted
and in the given language "baa" comes before
"abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.
Example 2:
Input:
N = 3, K = 3
dict = {"caa","aaa","aab"}
Output:
1
Explanation:
Here order of characters is
'c', 'a', 'b' Note that words are sorted
and in the given language "caa" comes before
"aaa", therefore 'c' is before 'a' in output.
Similarly we can find other orders.


Your Task:
You don't need to read or print anything. Your task is to complete the function findOrder() which takes  the string array dict[], its size N and the integer K as input parameter and returns a string denoting the order of characters in the alien language.

Expected Time Complexity: O(N * |S| + K) , where |S| denotes maximum length.
Expected Space Compelxity: O(K)

Constraints:
1 ≤ N, M ≤ 300
1 ≤ K ≤ 26
1 ≤ Length of words ≤ 50

"""
from collections import deque
class Solution:
    def findOrder(self,dict, N, K):

        adj = {}
        indegree = {}

        for lt in dict:
            for node in lt:
                indegree[node] = 0
                adj[node] = []

        # comparing string
        for i in range(len(dict) - 1):
            w1 , w2 = dict[i] , dict[i+1]
            minLen  = min(len(w1) , len(w2))
            for j in range(minLen):
                parent , child = w1[j] , w2[j]
                if parent != child:
                    adj[parent].append(child)
                    indegree[child] += 1
                    break

        # topological sort
        queue = deque()

        for key in indegree:
            if indegree[key] == 0:
                queue.append(key)

        topo = []

        while queue:
            node = queue.popleft()

            topo.append(node)

            for child in adj[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        if ( len(topo) != len(indegree) ):
            return ""

    # our topo is in list format so we need to convert into string
        return "".join(topo)
