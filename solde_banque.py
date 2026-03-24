solde = int(input("Entrez ici le solde"))
montant= int(input("Entrez le montant à retirer: "))
if montant<=solde:
    print("retrait effectué!")
else:
    print("solde insufisant")