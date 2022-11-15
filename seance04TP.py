from random import randint

def rollSecretCombination() -> list:
    secretCombination =[]
    while len(secretCombination) < 5:
        roll = randint(0,5)
        if COLORS[roll] not in secretCombination:
            secretCombination.append(COLORS[roll])
    return secretCombination

def convertProposalToList() -> list:
    return  proposal.split(',')

def verifPositions() -> (int, int):
    bienPlace = 0
    malPlace = 0
    for i in range(0,5):
        if proposal[i] == secret[i]:
            bienPlace += 1
        if proposal[i] in secret:
            malPlace += 1
    malPlace -= bienPlace
    return bienPlace, malPlace


if __name__ == "__main__":
    COLORS = [
        "Blanc",
        "Noir",
        "Jaune",
        "Vert",
        "Rouge",
        "Bleu"
    ]
    secret = rollSecretCombination()
    proposal = []
    nbCoups = 0
    print(secret)
    while proposal != secret:
        nbCoups +=1
        proposal = input("entrer les valeurs de la rangée séparées par une virgule : ")
        proposal = convertProposalToList()
        bienPlace, malPlace = verifPositions()
        print ("Pion bien placé : ", bienPlace, " | Pion mal placé : ", malPlace)

    print("Bravo vous avez gagné en ", nbCoups, " coups")

