from unittest import result


print("You will be getting all as result in an acronyme")
texte=str(input("Type here your name please"))

def accro_gen(chaine):
    mots=chaine.split()

    accro=""
    for i in mots:
        accro=accro+str(i[0]).upper
    return accro
résultat=accro_gen(texte)

print(résultat)