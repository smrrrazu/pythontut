# String is immutable, meaning we can not change it like list
# We can do dir(s) to see the list of functions name avaialbe in python
import time

str = "Hello Peter"
# print the string str
print(str)

# print lenth of the string str
print(len(str))

#print the string str from the offset 5
print(str[5:])

# We also can use string for the forloop
for x in str:
	print(x)
	#time.sleep(1)
# Checking the type of the variable
print(type(str))

# converting string to list type
l = list(str)
print('List of str is ',l)

# Joing all the value of the list with empty string and make a string
str2= ''.join(l)
print(str2)

# String find method

# This will print the offset of firt occured 'A' in the string 
print(str.find('A'))

# String replace method
print (str.replace('Hello','Parker'))



# spilting the string into a list
str3 = "aaa,bbb,cccc,ddddd"
print(str3.split(','))

# Making upper case
print (str.upper())

# Content test
print(str,"Hello World".isalpha())

# strip white spache from righ side
line = 'aaa,bbb,ccccc,dd\n'
print(line.rstrip())

# combine two operators
print(line.rstrip().split(","))

# Formating expression all
print('%s,%s and %s'%("Peter","Tom","Pol"))

# Formating method 2

str3 = '{0}, eggs, and {1}'.format('spam', 'SPAM!')
print(str3)

str3 = '{:,.2f}'.format(296999.2567)
print(str3)


