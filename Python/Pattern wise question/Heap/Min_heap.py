import heapq

lt = []

min_heap = heapq.heappush(lt , 0)
print(lt)
heapq.heappush(lt , 4)
print(lt)
heapq.heappush(lt , 3)
print(lt)
heapq.heappush(lt , 5)
print(lt)
heapq.heappush(lt , 6)
print(lt)
"""
[0]
[0, 4]
[0, 4, 3]
[0, 4, 3, 5]
[0, 4, 3, 5, 6]
"""
print("pop() is performing")
print(heapq.heappop(lt))
print(lt)
print(heapq.heappop(lt))
print(lt)
print(heapq.heappop(lt))
print(lt)
"""
pop() is performing
0
[3, 4, 6, 5]
3
[4, 5, 6]
4
[5, 6]

"""

print("heappushpop() Elements ::")
print(heapq.heappushpop(lt , 7))
print("Adding some elements")
heapq.heappush(lt , 8)
heapq.heappush(lt , 9)
heapq.heappush(lt , 5)
print(lt)
print("prforming heapreplace()")
print(heapq.heapreplace(lt , 2))
print(lt)
print("prforming heapreplace()")
print(heapq.heapreplace(lt , 7))
print(lt)

"""
heappushpop() Elements ::
5
Adding some elements
[5, 6, 8, 9, 7]
prforming heapreplace()
5
[2, 6, 8, 9, 7]
prforming heapreplace()
2
[6, 7, 8, 9, 7]
"""
print("nsmallest :: k = 2")
print(heapq.nsmallest(2, lt))
print("nlargest :: k = 2")
print(heapq.nlargest(2, lt))

"""
nsmallest :: k = 2
[6, 7]

nlargest :: k = 2
[9, 8]

"""

print("heapify () :: to sort all element")
lt1 = [1,7,2,9,3,4,5]
print(lt1)
heapq.heapify(lt1)
print(lt1)

"""
heapify () :: to sort all element
[1, 7, 2, 9, 3, 4, 5]
[1, 3, 2, 9, 7, 4, 5]
"""

print("priority queue :: ")

arr = [(1 ,2) , (1,3) , (2,1) , (2,4) , (0 ,1) , (0,3)]
print(arr)
heapq.heapify(arr)
print(arr)
"""
priority queue ::
[(1, 2), (1, 3), (2, 1), (2, 4), (0, 1), (0, 3)]
[(0, 1), (1, 2), (0, 3), (2, 4), (1, 3), (2, 1)]

"""

arr1 = [[1,2] , [1,2] , [0 , 1] , [0,2] , [2,1] , [2,2]]
print(arr1)
heapq.heapify(arr1)
print(arr1)

print("store pair on heapify()")
pair =[]
num = [2,3,5,1,6]
first = abs(num[1]-5)
print(first)
second = num[3]
print(second)

heapq.heappush(pair ,[first , second])
#heapq.heapify(first , second)
print(pair)
