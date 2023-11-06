pv = 0
pamet = 0
def multi(x:float, y:float)-> float:
    v = x*y
    global pv
    pv = v
    return v

def plus(x:float, y:float)-> float:
    v = x+y
    global pv
    return v

def uloz_posledni_vysledek():
    global pv
    return pv

def vrat_pamet():
    global pamet
    return pamet

def pricti_k_pameti(op:float):
    global pamet
    pamet += op
    return pamet

def vynasob_s_pameti(op:float):
    global pamet 
    pamet = pamet*op
    return pamet



    


