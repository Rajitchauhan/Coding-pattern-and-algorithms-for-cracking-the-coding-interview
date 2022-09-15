"""
Problem Statement #
Given an array of characters where each character represents a fruit tree,
you are given two baskets and your goal is to put maximum number of fruits in each basket.
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree.
You will pick one fruit from each tree until you cannot,
i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

def fruits_into_baskets(fruits):
  # TODO: Write your code here
  return -1

"""

class Solution:
    def fruits_into_baskets(self ,fruits):
        mini = float("-inf")
        beg  , last = 0 , 0
        ump = {}
        for last in range(len(fruits)):
            right = fruits[last]
            ump[right] = ump.get(right , 0) + 1
            while(len(ump) > 2):
                left = fruits[beg]
                ump[left] = ump.get(left , 0) - 1
                if(ump[left] == 0):
                    del ump[left]
                beg += 1
            mini = max(mini , last - beg + 1)
        return mini

if __name__ ==  "__main__":
    obj = Solution()
    lt = ['A', 'B', 'C', 'B', 'B', 'C']
    res = obj.fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])
    #obj.fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])
    print(f"maximum no of fruit {res}")
