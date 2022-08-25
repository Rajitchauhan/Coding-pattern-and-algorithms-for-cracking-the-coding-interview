import heapq

lt = []
print("heappush() in max heap")
heapq.heappush(lt , 0)
print(lt)
heapq.heappush(lt , 1)
print(lt)
heapq.heappush(lt , 5)
print(lt)
heapq.heappush(lt , 3)
print(lt)
heapq.heappush(lt , 7)
print(lt)
heapq.heappush(lt , 8)
print(lt)
print()
print("print whole list in positive numbers")
lt.reverse()
print(lt)
"""
[0]
[-1, 0]
[-5, 0, -1]
[-5, -3, -1, 0]

print whole list in positive numbers
[8, 5, 7, 0, 3, 1]
"""
print("heappop() in max heap")
print(heapq.heappop(lt))
print(lt)
print(heapq.heappop(lt))
print(lt)
print(heapq.heappop(lt))
print(lt)
"""
heappop() in max heap
-8
[-7, -5, -1, 0, -3]
-7
[-5, -3, -1, 0]
-5
[-3, 0, -1]

# add ' - ' in -heapq.heappop() ::
heappop() in max heap
8
[-7, -5, -1, 0, -3]
7
[-5, -3, -1, 0]
5
[-3, 0, -1]

"""
print("add some more elements")
heapq.heappush(lt , 9)
heapq.heappush(lt , 10)
heapq.heappush(lt , 11)
print(lt)
print()
print(" heapreplace() in max_heap ")
print(heapq.heapreplace(lt , -20))
print(lt)
print(heapq.heapreplace(lt , -10))
print(lt)
print(heapq.heapreplace(lt , -2))
print(lt)
print()
"""
add some more elements
[-11, -9, -10, 0, -3, -1]
 heapreplace() in max_heap
-11
[-20, -9, -10, 0, -3, -1]
-20
[-10, -9, -10, 0, -3, -1]
-10
[-10, -9, -2, 0, -3, -1]

"""
print()
print("nsmallest in max_heap")
# -i or abs(I)
lt2 = [-i for i in lt]
print(heapq.nsmallest(3 , lt2))

print("nlargest in max_heap")
print(heapq.nlargest(3 , lt2))
print()
"""
nsmallest in max_heap
[0, 1, 2]
nlargest in max_heap
[10, 9, 3]
"""
print("heapify in max_heap ")
new_heap = [2,4,6,1,3,9]
print(new_heap)
new_heap = [-i for i in new_heap]
heapq.heapify(new_heap)
print(new_heap)
print()
"""
heapify in max_heap
[2, 4, 6, 1, 3, 9]
[-9, -4, -6, -1, -3, -2]
"""
print("priority queue in max_heap")
arr = [(1 ,2) , (1,3) , (2,1) , (2,4) , (0 ,1) , (0,3)]
print(arr)

arr.reverse()
heapq.heapify(arr)
print(arr)
#[(0, 1), (0, 3), (1, 2), (2, 1), (1, 3), (2, 4)]
print("pair in max heap")
pair = []
first = abs(new_heap[0]-5)
print(first)
second = new_heap[1]
print(second)
heapq.heappush(pair , [first , second])
print(pair)
