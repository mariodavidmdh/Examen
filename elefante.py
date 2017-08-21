import animales

class elefante(animales.animal):
    def tomaragua(self,cantidadagua):
        self.cantidadagua+=cantidadagua
        print("El elefante tiene {0} litros de agua".format(self.cantidadagua))

    def alimentar(self,tipoalimento,cantidadalimento):
        if(tipoalimento.lower()=="mani"):
            self.cantidadalimento+=cantidadalimento
        else:
            print("solo me alimento de mani")
