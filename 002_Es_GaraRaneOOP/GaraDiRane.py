import random
import time
class Rana:

    def __init__(self,nome,peso):
        self.nome = nome
        self.peso = peso
        self.strada_percorsa = 0
        self.num_giri = 0



    def salto(self):

        self.set_stradaPercorsa(random.randint(30, 40) - (self.peso / random.randint(8, 12)))



    def set_stradaPercorsa(self,stradaPercorsa):

        self.strada_percorsa += stradaPercorsa



    def get_stradaPercorsa(self):

        return self.strada_percorsa



    def set_numGiri(self,giro):

        self.num_giri = giro



    def get_numGiri(self):

        return self.num_giri



    def get_nome(self):

        return self.nome



    def get_peso(self):

        return self.peso



    def __str__(self):

        return "Nome : "+self.get_nome()+" Peso : " + str(self.peso)



'''---------------------------------------------------------------------------------------------------------------------'''


class Gara:

    def __init__(self,lunghezzaPercorso,numPartecipanti):

        self.percorso = lunghezzaPercorso
        self.num_partecipanti= numPartecipanti
        self.lista_partecipanti = []



    def set_percorso(self,lunghezzaPercorso):

        self.percorso = lunghezzaPercorso



    def get_percorso(self):

        return self.percorso



    def get_listaPartecipanti(self):

        return self.lista_partecipanti



    def inserisci_partecipanti(self):

        for i in range(self.num_partecipanti):
            print("Inserire nome della rana", i + 1, ":")
            nome = input()
            peso = float(input("Il peso :\n"))
            self.lista_partecipanti.append(Rana(nome,peso))



    def get_datiGara(self):
        lista = self.get_listaPartecipanti()
        for i in range(len(lista)):
            print("La rana", lista[i].get_nome(), "che pesa", lista[i].get_peso(), "ha percorso",
                  lista[i].get_stradaPercorsa(),"cm", "che sta facendo il giro numero :",
                  lista[i].get_numGiri())
        return



    def svolgi_gara(self):
        gara_in_corso = True
        num_giri = 0;
        while (gara_in_corso):
            num_giri = num_giri + 1
            for i in range(len(self.get_listaPartecipanti())):
                if gara_in_corso:
                    self.get_listaPartecipanti()[i].salto()
                    self.get_listaPartecipanti()[i].set_numGiri(num_giri)
                if self.get_listaPartecipanti()[i].get_stradaPercorsa()>= 600:
                    gara_in_corso = False
            print("NUMERO GIRO :", num_giri)
            self.get_datiGara()
            time.sleep(1)


'''---------------------------------------------------------------------------------------------------------------------'''





gara = Gara(600,3)
gara.inserisci_partecipanti()
gara.svolgi_gara()


lista = sorted(gara.get_listaPartecipanti(), key=lambda Rana: Rana.get_stradaPercorsa(), reverse=True)
print((lista))