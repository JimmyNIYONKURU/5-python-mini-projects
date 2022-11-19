import random
print("Appuyez 1 pour lancer le dé et 0 pour quitter le programme")
while True :

    x=int(input("Clic here"))

    if x==0 :
        print("Bye and thank you")
        break

    elif x==1 :
        print(random.randint(1,6))
    
    else :
        print("You've committed a mistake! You shoud try again")