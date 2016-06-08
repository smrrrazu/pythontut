str1 = "Test string global"


def f1():
    str2 = "Test string local"
    print(str1)
    print(str2)
    # print (locals())

# f1()
# print (globals())
# print(str1)


def foo(x):
    print(locals())

foo(1)

print(foo.__class__)
