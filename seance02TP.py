from random import randint
import sandbox

if __name__ == "__main__":
    encore = True
    while encore:
        nbCoups = 0
        partieEnCours = True
        tirage = randint(0, 50)
        # print(tirage)

        while partieEnCours:
            nbCoups += 1
            proposal = int(input("Sasir un nombre entre 1 et 50"))
            if proposal == tirage:
                if tirage in {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47}:
                    nbCoups-=1
                    print("Vous avez gagné en ", nbCoups, "coup(s) (BONUS NOMBRE PREMIER")
                else:
                    print("Vous avez gagné en ", nbCoups, " coup(s)")
                partieEnCours = False
            elif proposal > tirage:
                print("plus petit")
            else:
                print("plus grand")

        autrePartie = input("Voulez vous continuer (o/n) ?")
        if autrePartie == 'n':
            encore = False

