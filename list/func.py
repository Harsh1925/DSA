mylist = ["banana", "cherry", "apple"]
print(mylist)

item = mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

newlist = [5, 3, 7, -1, 10]
print(newlist)
print("")

sortlist = sorted(newlist)
print(sortlist)
print(newlist)

print("")

item = newlist.sort()
print(newlist)

conclist = mylist + newlist
print(conclist)

print("")

praclist = [1,2,3,4,5,6,7,8]

a = praclist[1::2]
print(a)

a = praclist[::-1]
print(a)

b = [i*i for i in praclist]
print(b)
print(praclist)

"""
['banana', 'cherry', 'apple']
['apple', 'cherry', 'banana']
['apple', 'banana', 'cherry']
[5, 3, 7, -1, 10]

[-1, 3, 5, 7, 10]
[5, 3, 7, -1, 10]

[-1, 3, 5, 7, 10]
['apple', 'banana', 'cherry', -1, 3, 5, 7, 10]

[2, 4, 6, 8]
[8, 7, 6, 5, 4, 3, 2, 1]
[1, 4, 9, 16, 25, 36, 49, 64]
[1, 2, 3, 4, 5, 6, 7, 8]
"""