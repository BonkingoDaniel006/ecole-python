inscrits = {"Alice", "Bob", "Charlie", "Diana"}
presents = {"Alice", "Charlie", "Eve"}

absent= inscrits - presents
print(absent)

non_inscrits= presents - inscrits

print(non_inscrits)

present_inscrits= inscrits & presents

print(present_inscrits)