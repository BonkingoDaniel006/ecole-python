n=1
print("tentative: ", n, ".")

password= input("Saisissez votre mot de passe: ")


while password!="secret123":
    n=n+1
    print("tentative: ", n, ".")
    password= input( "Saisissez votre mot de passe: ")

if password == "secret123":
        print("Accès autorisé")
        print("Nombre de tentatives: ", n)