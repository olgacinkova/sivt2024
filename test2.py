def k_prumer(vstup: list[float]) -> float:
    vystup = 0
    n = len(vstup)
    for x in vstup:
        vystup += x **2
    vystup = vystup/n
    return vystup

def testuj(seznam: list[float]) -> float:
    print(k_prumer(seznam))
    return True

testuj([1,2,3,4])
