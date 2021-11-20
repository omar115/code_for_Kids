A = int(input("Please provide te value>>"))
B = int(input("Please provide te value>>"))
C = int(input("Please provide te value>>"))
D = int(input("Please provide te value>>"))

if B > C and D > A: 
    if (C+D) > (B+A):
        if C > 0 and D > 0:
            if A % 2 == 0:
                print("Valores aceitos")
else: 
    print("Valores nao aceitos")