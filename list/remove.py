mylist = ["banana", "cherry", "apple"]
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

mylist = ["banana","cherry","apple"]
print("new list =", mylist)
item = mylist.remove("cherry")
print(item)
print(mylist)

mylist.clear()
print(mylist)

"""
['banana', 'cherry', 'apple']
apple
['banana', 'cherry']

new list = ['banana', 'cherry', 'apple']
None
['banana', 'apple']

[]

"""


"""
['banana', 'cherry', 'apple']
apple
['banana', 'cherry']
"""