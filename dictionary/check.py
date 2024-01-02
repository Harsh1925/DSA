mydict = {"name": "Max", "age": 23, "city": "New York"}

print(mydict)

if "name" in mydict:
    print(mydict["name"])  #Max

for key in mydict:
    print(key)

"""
name
age
city

"""

for key in mydict.keys():
    print(key)

"""
name
age
city
"""

for value in mydict.values():
    print(value)

"""
Max
23
New York
"""

for key,value in mydict.items():
    print(key, value)

"""
name Max
age 23
city New York
"""