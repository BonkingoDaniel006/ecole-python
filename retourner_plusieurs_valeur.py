#fonction
def stats(notes):
    a=notes[0]
    b=notes[1]
    c=notes[2]
    d=notes[3]
    e=notes[4]
    moy= (a+b+c+d+e)/2
    print (f"Moyenne: {moy}")
    minimum= min(notes)
    maximum= max(notes)
    print(f"Min: {minimum}")
    print(f"Max: {maximum}")


#debut du code
cote=  [12, 8, 15, 10, 18]

stats(cote)