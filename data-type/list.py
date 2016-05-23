# List type variable

L = [123, 'spam', 1.23]

# Lenth of list
print("Lenth of the list: %2d " % len(L))

# Indexing by position
print(L[0])

# Slicing listh
print(L[:2])

# Concating List
print(L+[4,5,6])
print(L*3)
print(L)
# Delete from the list
del(L[0])
L.pop(1)

print(L)

L = [1,6,7,4]
L.sort()
print(L)
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]
L = [a,b,c]
print(L[1])

