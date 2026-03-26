liste = [[1, 2], [3, 4], [5, 6, 7]]
a=[]

for i in range(0,2):
    b=liste.pop([i], [0])
    c=liste.pop([i], [1])
    print(b,c)