# definicion de la clase Vehiculo
class Vehiculo:

    # constructor de la clase Vehiculo
    def __init__(self, matricula, color, nuemeroPuertas):
        self.MATRICULA = matricula
        self.COLOR = color
        self.NUMERO = nuemeroPuertas
        self.AVANZA = False
        print("construccion de un vehiculo : " + self.MATRICULA)

    # Metodo avanzar
    def Avanzar(self):
        self.AVANZA = True
        print(self.MATRICULA + "avanza.")

    # Metodo de detenerse
    def Detenerse(self):
        self.Avanzar = False
        print(self.MATRICULA + "se detiene.")

# constrauccion de una primera instancia
vehiculo1 = Vehiculo("AR123", "azul", 4)


# construccuin de segunda instancia 
vehiculo2 = Vehiculo("FR456", "verde", 5)

# el primer vehiculo avanza
vehiculo1.Avanzar()

# el primer vehiculo de detiene
vehiculo1.Detenerse()

# en la linea (1,3) es para iniciar el programa
# en la linea (4,10) es para crear el vehiculo la matricula el color y las puertas
# en la linea (11,15) espara que el vehicul avanse 
# en la linea (16,20) es para que el vehiculo de detenga
# en la linea (22,33) es para la cnstruccion del vehiculo 1 y la construccion del vehiculo 2 es para que el carro 1 avanse y se detenga 