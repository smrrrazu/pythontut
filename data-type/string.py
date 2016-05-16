import time
str = "Hello Afsheen"
print(str)
print(len(str))
print(str[5:])
for x in str:
	print(x)
	#time.sleep(1)

print(type(str))

# converting string to list type
l = list(str)
print('List of str is ',l)

str2= ''.join(l)
print(str2)




