import fonctionsTP.fonctionsTP3
from random import randint


def saisie_nombre(nbMin: int, nbMmax: int) -> int:
    while True:
        res = input("Sasir un nombre entre 1 et 50")
        if res.isnumeric():
            if nbMin <= int(res) <= nbMmax:
                break
    return int(res)


def is_parfait(nb: int) -> bool:
    div = 0
    res = True
    for i in range(1, nb):
        if nb % i == 0:
            div += i
    if nb != div:
        res = False
    return res


if __name__ == "__main__":

    encore = True
    while encore:
        nbCoups = 0
        partieEnCours = True
        tirage = randint(1, 50)

        while partieEnCours:
            nbCoups += 1
            proposal = saisie_nombre(1, 50)
            isEqual, message = fonctionsTP.fonctionsTP3.test_nombre(tirage, proposal)
            if isEqual:
                if fonctionsTP.fonctionsTP3.is_premier(tirage):
                    nbCoups -= 1
                    print(tirage, " est un nombre premier (bonus)")
                if is_parfait(tirage):
                    nbCoups += 1
                    print(tirage, " est un nombre parfait (malus)")
                print("Vous avez gagné en ", nbCoups, " coup(s)")
                partieEnCours = False
            else:
                print(message)

        autrePartie = input("Voulez vous continuer (o/n) ?")
        if autrePartie == 'n':
            encore = False
