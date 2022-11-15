def test_nombre(tirage: int, proposal: int) -> [bool, str]:
    res = True
    message = "egalite"
    if tirage != proposal:
        res = False
        if proposal < tirage:
            message = "Plus grand"
        else:
            message = "Plus petit"
    return res, message


def is_premier(nb: int) -> bool:
    premier = True
    i = 2
    while i < nb:
        if nb % i == 0:
            premier = False
            break
        i += 1
    return premier
