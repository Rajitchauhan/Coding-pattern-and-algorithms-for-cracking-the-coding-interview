"""
Given number of pages in n different books and m students. The books are arranged in ascending order of number of pages. Every student is assigned to read some consecutive books. The task is to assign books in such a way that the maximum number of pages assigned to a student is minimum.
Example :


Input : pages[] = {12, 34, 67, 90}
        m = 2
Output : 113
Explanation:
There are 2 number of students. Books can be distributed
in following fashion :
  1) [12] and [34, 67, 90]
      Max number of pages is allocated to student
      2 with 34 + 67 + 90 = 191 pages
  2) [12, 34] and [67, 90]
      Max number of pages is allocated to student
      2 with 67 + 90 = 157 pages
  3) [12, 34, 67] and [90]
      Max number of pages is allocated to student
      1 with 12 + 34 + 67 = 113 pages

Of the 3 cases, Option 3 has the minimum pages = 113.

"""

def pages_allocaation(arr , k , n):
    low = max(arr)
    high = sum(arr)
    if k>n:
        return - 1
    while(low<=high):
        mid = low + (high-low)//2
        if (isValid(arr , n , k , mid) == True):
            res = mid
            high = mid-1
        else:
            low = mid+1
    return res

def isValid(arr , n , k , mid):
    student = 1
    sum = 0
    for i in range(n):
        sum = sum + arr[i]
        if sum > mid:
            student = student + 1
            sum = arr[i]

        if student > k:
            return False
    return True

def sum(arr):
    s = 0
    for i in range(len(arr)):
        s = s+ arr[i]
    return s
def max(arr):
    n=len(arr)
    if sorted(arr) == arr:
        return arr[n-1]


arr= [10,20,30,40]
arr=[12, 34, 67, 90]
k = 2
n = len(arr)
print(pages_allocaation(arr , k , n))
