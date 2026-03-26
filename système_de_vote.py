vote=0
A=0
B=0
C=0
while vote<6:
    vote= vote+1
    print(f"vote: {vote}")
    print("1.ALICE")
    print("2.BOB")
    print("1.CHARLIE")
    v=int(input("Inscrivez ici votre choix: "))
    if v==1:
        A=A+1
    elif v==2:
        B=B+1
    elif v==3:
        C=C+1


print(f"Alice a {A} vote(s)")
print(f"BOB a {B} vote(s)")
print(f"CHARLIE a {C} vote(s)")

if A>B and A>C:
    print("Gagnant: Alice")
elif B>A and B>C:
    print("Gagnant: BOB")
elif C>A and C>B:
    print("Gagnant: CHARLIE")