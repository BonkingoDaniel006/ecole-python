liste =  ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
liste2= set(liste)
print(liste)
print(liste2)
a= len(liste2)
b= len(liste)
c= b-a
print(f"il y'a {a} prenoms distinct")
print(f"{c} on été supprimé car c'etait des doublons.")