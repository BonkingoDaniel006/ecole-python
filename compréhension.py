carre = [4, 16, 36, 64, 100] 
dictionnaire = {
    "mot": "longueur"
}
liste= ["python", "est", "cool"]
liste2= ["Alice", "Bob", "Anna", "Charlie", "Brice"]
nom1= liste2[0]
nom2= liste2[1]
nom3= liste2[2]
nom4= liste2[3]
nom5= liste2[4]
lettre1= nom1[0]
lettre2= nom2[0]
lettre3= nom3[0]
lettre4= nom4[0]
lettre5= nom5[0]

liste_initial = []

liste_initial.extend([lettre1,lettre2,lettre3,lettre4,lettre5])
set_initial = set(liste_initial)
print(set_initial)