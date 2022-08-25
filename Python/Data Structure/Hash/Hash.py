def display_hash(hashTable):
	for i in range(len(hashTable)):
		print(" " , end= " ")

		for j in range(i+1):
			print("-->" , end=" ")
			print(j , end=" ")
		print()

#creating hash as a neasted  list

hashTable = [[] for _ in range(10)]
"""  
# function return key for every value

def hashing(keyvalue):
	return keyvalue % len(hashTable)

def insert(hashTable , keyvalue , value):
	has_key = hashing(keyvalue)
	hashTable[has_key].append(value)

insert(hashTable , 10 , "agra")
insert(hashTable , 15 , "Eta")
insert(hashTable , 11 , "mathura")
insert(hashTable , 10 , "agra")
insert(hashTable , 13 , "aligarh")
insert(hashTable , 12 , "delhi")
insert(hashTable , 11 , "mathura")
insert(hashTable , 10 , "agra")
"""
display_hash(hashTable)