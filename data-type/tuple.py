T = (1, 1, 2, 3, 4)
# print first element
print(T[0])

# Length
print(len(T))

# Concate
T += (5, 6)
print(T)

# index function return the index number by match value
# if multiple values available then first one is selected 
print(T.index(1))

# count() function is used to count how many time the passing 
# element avialbel in the tuple
print(T.count(1))

# tuple are immutable, meaning we can not change it


try:
	T[0]=2
except TypeError:
	print("Type Error happen")

T1 = 1, 3, "Bangladesh", [3.5, 500, 'Dhaka'], {'name':"Sheikh Razu"}
print(T1)
print(type(T1[3]))
print(type(T1))
print(type(T1[4]))

