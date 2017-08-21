import animales

class conejo(Animales. Animal):
    def Alimentar(self,tipoalimento,cantidadalimento):
        if(tipoalimento=="pasto"):
            self.cantidadalimento+=cantidadalimento
            self.tipoalimento=tipoalimento

    def correr(self):
        if(self.cantidadalimento>0):
            self.cantidadalimento-=1
            print(self.cantidadalimento)
        else:
            print("Estoy cansado y hambriento")
