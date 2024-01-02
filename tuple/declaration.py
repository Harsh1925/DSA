mytuple = ("max",28,"Boston")
print(mytuple)
#('max', 28, 'Boston')

secTuple = tuple(["max",28,"Boston"])
print(secTuple)
#('max', 28, 'Boston')

newTuple = "max",28,"boston"
print(mytuple)
print(type(newTuple))
#('max', 28, 'Boston')
#<class 'tuple'>

fakeTuple = ("max")
print(fakeTuple)
#max
#<class 'str'>

print(type(fakeTuple))

trueTuple = ("max",)
print(trueTuple)
print(type(trueTuple))
#('max',)
#<class 'tuple'>

mylist = list(mytuple)
print(mylist)
#['max', 28, 'Boston']

mytuple = tuple(mylist)
print(mytuple)
#('max', 28, 'Boston')

name, age, city = mytuple
print(name)
print(age)
print(city)
"""
max
28
Boston

"""

pracTuple = (0,1,2,3,4)

i1, *i2, i3 = pracTuple

print(i1)
print(i2)
print(i3)

"""
0
[1, 2, 3]  it is converted to list
4

"""