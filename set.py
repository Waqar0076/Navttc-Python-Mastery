# creating sets
A = {20, 10, 50, 60, 100, 5}
B = {70, 60, 40, 30, 2, 5}
C = {70, 160, 40, 130, 2, 5}

# Add element in set A
A.add(2)
print(A)

# merging multiple sets in set A
# deals with multiple sets
A.update(B,C)
print(A)

#removing element
A.remove(5) 	
print(A)

A.pop()
A.pop()
print(A)


# print("--- Union of Sets is -------")
print(A.union(B))

# print("--- intesection of Sets is -------")
print(A.intersection(B))

# print("--- Difference of 2 Sets is -------")
print(A.difference(B))

# print("--- Symmectric Difference of 2 Sets is -------")
print(A.symmetric_difference(B))

# print(A)
# print(type(A))