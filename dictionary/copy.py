mydict = {"name": "Max", "age": 23, "city": "New York"}

mydict_cpy = mydict

mydict_cpy["email"] = "Max@gmail.com"

print(mydict) #{'name': 'Max', 'age': 23, 'city': 'New York', 'email': 'Max@gmail.com'}

print(mydict_cpy) #{'name': 'Max', 'age': 23, 'city': 'New York', 'email': 'Max@gmail.com'}


mydict = {"name": "Max", "age": 23, "city": "New York"}

mydict_cpy = mydict.copy()
mydict_cpy["email"] = "Max@gmail.com"

print(mydict) #{'name': 'Max', 'age': 23, 'city': 'New York'}
print(mydict_cpy) #{'name': 'Max', 'age': 23, 'city': 'New York', 'email': 'Max@gmail.com'}



mydict = {"name": "Max", "age": 23, "city": "New York"}

mydict_cpy = dict(mydict)
mydict_cpy["email"] = "Max@gmail.com"

print(mydict) #{'name': 'Max', 'age': 23, 'city': 'New York'}
print(mydict_cpy) #{'name': 'Max', 'age': 23, 'city': 'New York', 'email': 'Max@gmail.com'}
