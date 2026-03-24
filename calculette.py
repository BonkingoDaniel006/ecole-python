n1 = float(input("Entrez le premier nombre: "))
n2 = float(input("Entrez le second nombre: "))
print("Entrez l'opération.")
print("1. Addition")
print("2. Soustraction")
print("3. division")
print("4. multiplication")
n3= int(input("entrez l'opération: "))

if n3==1:
    r=n1+n2
    print(r)
elif n3==2:
    r= n1-n2
    print(r)
elif n3==3:
    r= n1/n2
    print(r)
elif n3==4:
    r= n1*n2
    print(r)