liste = [1, 2, 2, 3, 4, 4, 4, 5]
doublon= []
for i in range(1, 6):
    
    a= liste.count(i)
    if a>1:
        n= liste[i]
        doublon.append(n)
    
print(doublon)

