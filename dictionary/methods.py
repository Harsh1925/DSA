capitals = {"USA": "Washing D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"
            }
print(capitals)
print(capitals.get("India")) #New Delhi

if capitals.get("Russia"):
    print("That capital exists", capitals.get("Russia"))
    
else:
    print("Not exists")

if capitals.get("Japan"):
    print("That capital exists", capitals.get("Russia"))
    
else:
    print("Not exists")


capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "New York"})
print(capitals)
#{'USA': 'New York', 'India': 'New Delhi', 'China': 'Beijing', 'Russia': 'Moscow', 'Germany': 'Berlin'}

keys = capitals.keys()
print(keys)
#dict_keys(['USA', 'India', 'China', 'Russia', 'Germany'])

values = capitals.values()
print(values)
#dict_values(['New York', 'New Delhi', 'Beijing', 'Moscow', 'Berlin'])

items = capitals.items()
print(items)
#dict_items([('USA', 'New York'), ('India', 'New Delhi'), ('China', 'Beijing'), ('Russia', 'Moscow'), ('Germany', 'Berlin')])

for key,value in capitals.items():
    print(f"{key}: {value}")

"""
USA: New York
India: New Delhi
China: Beijing
Russia: Moscow
Germany: Berlin
"""
