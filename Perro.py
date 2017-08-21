import Animales

class perro(Animales,Animal):
    def TomarAgua(self,cantidadagua):
        self.cantidadagua+=cantidadagua
        print("El perro tiene {0} litros de agua".format(cantidadagua))
        def Alimentar(self,tipoalimento,cantidadalimento):
            if(tipoalimento=="Dogui"):
                self.cantidadalimento+=cantidadalimento
            else:
                print("El perro solo come Dogui")
