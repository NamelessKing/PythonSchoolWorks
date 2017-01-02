import random
import time
try:
    num_partecipanti = int(input("Quante rane devono gareggiare? \n"))
except ValueError:
    print("ERRORE: Inserire un numero intero")

print(num_partecipanti,"rane in gara ")

rane = [[]]*num_partecipanti

def salto(peso):
    return random.randint(30,40)-(peso/random.randint(8,12))

def dati_gara(lista):
    for i in range(len(lista)):
        print("La rana",lista[i][0],"che pesa",lista[i][1],"ha percorso",lista[i][2],
              "cm","che sta facendo il giro numero :",lista[i][3])
    return;

for i in range(num_partecipanti):
    print("Inserire nome della rana",i+1,":")
    nome = input()

    try:
        peso = int(input("Il peso :\n"))
    except ValueError:
        print("ERRORE: Inserire un numero intero")

    strada_percorsa = 0.0

    num_giri = 0

    rane[i] = [nome,peso,strada_percorsa,num_giri]

print("Statistiche delle rane :")
for i in range(num_partecipanti):
    print(rane[i])

print("\n")

gara_in_corso = True
num_giri = 0;

while(gara_in_corso):
    num_giri = num_giri+1
    for i in range(num_partecipanti):
        if gara_in_corso:
            peso = rane[i][2]
            rane[i][2] = peso + salto(rane[i][1])
            rane[i][3] = num_giri
        if rane[i][2] >= 600:
            gara_in_corso = False
    print("NUMERO GIRO :", num_giri)
    dati_gara(rane)
    time.sleep(1)


rane = sorted(rane, key=lambda x:x[2],reverse=True)

print("Classifica :")
for i in range(num_partecipanti):
    print(rane[i])
