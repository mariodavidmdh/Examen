import datetime
class animal:
    def __init__(self,reproduccion,cantidadanimales):
        self.animalesreproduccion =reproduccion
        self.cantidadanimales = cantidadanimales
        self.nacimiento = []
        self.fechanacimiento=[]
        self.tipoalimento=""
        self.cantidadalimento=0
        self.cantidadagua=0

    def __nacimiento(self,hembraprenadas):
        nacidos = (self.animalesreproduccion*hembraprenadas)
        self.cantidadanimales+=nacidos
        self.fechanacimiento.append(datetime.datetime.today())
        self.nacimiento.append(nacidos)
        print("La cantidad de animales nacidos es {0} ahora tiene {1} animales".format(nacidos,self.cantidadanimales))

    def reproduccion(self,cantidadanimales):
        if(self.cantidadanimales>cantidadanimales):
            self.__nacimiento(cantidadanimales)
        else:
            print("La cantidad animales en reproducion no")
            ("puede ser mayor a la cantidad de animales axistente")

    def decesos(self, cantidaddecesos):
        self.cantidadanimales-=cantidaddecesos
        print("La cantidad actual de animales es {0}".format(self.cantidadanimales))

    def imprimirtodo(self):
        rango =len(self.nacimiento)
        print("cantidad\tfecha de nacimiento")
        if(rango>0):
            for elemento in range(rango):
                print("{0}\t\t{1}".format(self.nacimiento[elemento],self.fechanacimiento[elemento]))
        elif(rango==0):
            print("{0}\t\t{1}".format(self.nacimiento[0],self.fechanacimiento[0]))
        else:
            print("No existen partos recientes")
