fruits = {
    "pomme": 10,
    "banane": 5, 
    "orange": 8
}

p= fruits["pomme"]
print (f"Il y'a {p} pommes")

fruits["orange"] = 11
print(fruits)

for nom ,note in fruits.items():
    if note>6:
        print(nom)