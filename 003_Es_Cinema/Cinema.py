"""Creare il programma in Python funzionale che simuli la situazione esposta in seguito (completo di FlowChart ) 

Si vuole realizzare un software che gestisca tre sale cinematografiche.
La SalaCinema ha il seguente insieme di attributi minimali: film (nome del film proiettato),
prezzoFilm (prezzo di un singolo biglietto),
numero di file (numero di file degli spettatori),
maxPerFila (numero massimo di spettatori per fila), posti Occupati (nr di biglietti già venduti per la sala), incasso.

Il software gestirà l'accesso alle sale tramite vendita di biglietti.
L'operatore in cassa dovrà richiedere il titolo del film, che il cliente vuole vedere,
e procedere alla vendita dei biglietti (senza che il biglietto sia assegnato ad un posto preciso);
quindi all’aggiornamento della situazione prima del cliente successivo.

In ogni momento deve essere possibile stampare un repoert sull'occupazione delle sale (posti liberi e occupati)
e incasso effettuato"""

import time

#Variabili usati come indice per puntare sulle sale del cinema dove ogni sala corrisponde a una riga della matrice che verra
#costruito piu avanti Es. cinema[s1][n] corrisponde alla sala 1

s1 = 0
s2 = 1
s3 = 2


#Variabili da usare come indice nelle liste delle sala,chiamandoli come gli atributi della sala per facilitare il lavoro
nome_film = 0
prezzo_biglietto = 1
num_file = 2
max_spet_fila = 3  #indice per il numero massimo di spettatori per fila
posti_occupati = 4
incasso = 5


#Matrice chiamato "cinema " dove ogni fila corrisponde ad una sala con i relativi dati

cinema =[["Pirati dei Caraibi 5",8.50,3,5,0,0],
         ["The Avengers 3",8.00,2,3,0,0],
         ["Il Signore degli Anelli",10.00,5,2,0,0]]



#Funzione che mostra la situazione attuale delle sale
def datiSale(cinema):
    for i in range(len(cinema)):
        print("Sala ",i+1,"\n  Film :",cinema[i][nome_film],"\n  Prezzo biglietto : ",cinema[i][prezzo_biglietto],"euro",
              "\n  Posti disponibili : ",(cinema[i][num_file]*cinema[i][max_spet_fila])- cinema[i][posti_occupati],
              "\n  Posti occupati : ",cinema[i][posti_occupati],
              "\n  Incasso : ",cinema[i][incasso],"euro.")

#Funzione che restituisce i posti disponibile data l'indice di una sala
def postiDisponibili(num_sala):
    return (cinema[num_sala][num_file]*cinema[num_sala][max_spet_fila])- cinema[num_sala][posti_occupati]

def isSalaPiena(num_sala):
    return cinema[num_sala][posti_occupati] == cinema[num_sala][num_file]*cinema[num_sala][max_spet_fila]


#Variabile booleano che controlla la disponibilita dei posti nelle sale  che verrà messo come condizione dell while dove
#se ce almeno un posto libero in uno delle sale,l'operatore attendera altri clienti

disponibilita = True;
while (disponibilita) :
    #Mostra i film priettati nelle sale
    print("\nFILM PRIOIETTATI :\n",
          "PREMERE [1] PER GUARDARE. ",cinema[s1][0],"\n",
          "PREMERE [2] PER GUARDARE. ",cinema[s2][0],"\n",
          "PREMERE [3] PER GUARDARE. ",cinema[s3][0],"\n",
          "PREMERE [4] PER VEDERE IL REPORT  DELLE SALE \n")

    #Scelta del'operazione da parte dell'utente
    scelta_operazione = int(input("SCEGLIERE L'OPERAZIONE DA EFFETTUARE TRA : [1] [2] [3] [4] \n"))

    #Scelta per per visualizzare i dati delle sale
    if(scelta_operazione == 4):
        datiSale(cinema)
        time.sleep(2)
    elif (scelta_operazione >=1 and scelta_operazione <=3):#Controllo se l'utente ha fatto un inserimento della scelta del film e giusta,solo se vera si procede

        #Se la sala scelta non è ancora piena,si continua con le operazioni
        if(not isSalaPiena(scelta_operazione-1)):

            #'Controlla se ci sono ancora posti disponibili nella sala scelta
            if( postiDisponibili(scelta_operazione-1)>0):

                #Stama i posti disponibili
                print("Sono disponibili : ",postiDisponibili(scelta_operazione-1)," posti\n")


                #Inserimento del numero di spettatori
                num_spettatori = int(input("Inserire il numero di spettatori: \n"))

                #Se ci sono abbastanza posti per per gli spettatori appena arrivati,vengono consegnati i biglietti e
                #viene aggiornato la situazione della sala
                if(num_spettatori <= postiDisponibili(scelta_operazione-1)):
                    print("Ci sono ancora posti disponibili per voi!!!\nEcco a voi",num_spettatori,"biglietti/o")
                    cinema[scelta_operazione-1][posti_occupati] += num_spettatori
                    cinema[scelta_operazione-1][incasso] += cinema[scelta_operazione-1][prezzo_biglietto]*num_spettatori
                    time.sleep(2)
                #Se ci sono troppi spettatori appena arrivati rispetto ai posti ancora disponibili,
                # si ritorna alla scelta delle operazioni
                else:
                    print("Non ci sono abbastanza posti disponibili per", num_spettatori, "spettatori")
                    time.sleep(2)

        else:
            print("LA SALA E PIENA\n")
            time.sleep(1)

    else:
        print("Scelta non valida,riprovare..\n")
        time.sleep(1)

    if(isSalaPiena(s1)and isSalaPiena(s2) and isSalaPiena(s3)):
        disponibilita = False
        print("\nTUTTE LE SALE SONO PIENE,ARRIVEDERCI")











