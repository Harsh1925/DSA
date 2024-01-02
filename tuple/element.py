mytuple = ("max", 20, "Boston")

item = mytuple[0]
print(mytuple)
print(item)

for i in mytuple:
    print(i)

if "max" in mytuple:
    print("yes")

newTuple = ('a','b','c','a','v','e','a')

print(len(newTuple)) #7

print(newTuple.count('a')) #3
print(newTuple.count('b')) #1
print(newTuple.count('r')) #0

print(newTuple.index('c')) #2

b = newTuple[2:5]
print(b)
#('c', 'a', 'v')