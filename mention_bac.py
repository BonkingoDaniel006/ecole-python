mention = float(input("Entrez votre cotation: "))
if mention>=16:
    print("votre mention est: très bien")
else:
    if mention>=14:
        print("votre mention est: bien")
    else: 
        if mention>=12:
            print("votre mention est: assez bien")
        else:
            if mention>=10:
                print("votre mention est: passable")
            else:
                if mention<10:
                    print("insuffisant.")