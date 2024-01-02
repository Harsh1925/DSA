list_org=["banana","cherry", "apple"]

list_cpy = list_org

list_cpy.append("lemon")

print(list_cpy) #['banana', 'cherry', 'apple', 'lemon']
print(list_org) #['banana', 'cherry', 'apple', 'lemon']

list_org=["banana","cherry", "apple"]

list_cpy = list_org.copy()

list_cpy.append("lemon")

print(list_cpy) #['banana', 'cherry', 'apple', 'lemon']
print(list_org) #['banana', 'cherry', 'apple']


list_org=["banana","cherry", "apple"]

list_cpy = list(list_org)

list_cpy.append("lemon")

print(list_cpy) #['banana', 'cherry', 'apple', 'lemon']
print(list_org) #['banana', 'cherry', 'apple']

list_org=["banana","cherry", "apple"]

list_cpy = list_org[:]

list_cpy.append("lemon")

print(list_cpy) #['banana', 'cherry', 'apple', 'lemon']
print(list_org) #['banana', 'cherry', 'apple']