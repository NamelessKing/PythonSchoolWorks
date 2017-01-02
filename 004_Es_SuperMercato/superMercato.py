acquisti = ["banana","arancia","pere","aaaaaa"]

scafale = {"banana":6,"mela":0,"arancia":32,"pere":15,"uva":20}

prezzi = {"banana":4,"mela":3,"arancia":1.5,"pere":13}

def calcolo_prezzo(lista):

    tot = 0
    for i in acquisti:
        tot += prezzi.get(i,0)
    return tot

def calcolo_prezzo_aggiorna_scafale(lista):

    tot = 0
    for i in acquisti:
        if(scafale.has_key(i)== 1 and scafale[i] > 0):
            tot += prezzi[i]
            scafale[i]-= 1

    return tot



print (calcolo_prezzo(acquisti))
print (calcolo_prezzo_aggiorna_scafale(acquisti))
print (scafale)