# Ex 1049
P1 = input()
P2 = input()
P3 = input()

if P1 == "vertebrado":
    if P2 == "ave":
        if P3 == "carnivoro":
            print("aguia")
        elif P3 == "onivoro":
            print("pomba")
    elif P2 == "mamifero":
        if P3 == "onivoro":
            print("homem")
        elif P3 == "herbivoro":
            print("vaca")
elif P1 == "invertebrado":
    if P2 == "inseto":
        if P3 == "hematofago":
            print("pulga")
        elif P3 == "herbivoro":
            print("lagarta")
    elif P2 == "anelideo":
        if P3 == "hematofago":
            print("sanguessuga")
        elif P3 == "onivoro":
            print("minhoca")
