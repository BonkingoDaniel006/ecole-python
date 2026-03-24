age = int(input("Entrez votre age: "))
if age>25:
    print("le ticket coute 12$")
else:
    if age >= 12:
        print("les ticket est à 9$")
    else:
        if age<12:
            print ("le ticket est à 6$")