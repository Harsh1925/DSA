mydict = {"name": "Max", "age":28,"city":"New York"}
print(mydict)

del mydict["name"]
print(mydict)
#{'age': 28, 'city': 'New York'}

mydict = {"name": "Max", "age":28,"city":"New York"}
print(mydict)

mydict.pop("age")
print(mydict)
#{'name': 'Max', 'city': 'New York'}

mydict = {"name": "Max", "age":28,"city":"New York"}
print(mydict)

mydict.popitem() #remove last item
print(mydict)
#{'name': 'Max', 'age': 28}