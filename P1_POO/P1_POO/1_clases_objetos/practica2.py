"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches
class Coches:

    # Atributos privados
    def __init__(self, color, marca, velocidad):
        self.__color = color
        self.__marca = marca
        self.__velocidad = velocidad

    # Métodos
    def acelerar(self, incremento=10):
        self.__velocidad += incremento
        return self.__velocidad

    def frenar(self, decremento=10):
        self.__velocidad = max(0, self.__velocidad - decremento)
        return self.__velocidad

    def toca_claxon(self):
        return "¡Bip, bip!"

    def get_color(self):
        return self.__color

    def get_marca(self):
        return self.__marca

    def get_velocidad(self):
        return self.__velocidad
        
#isntaciar o crear objetos de la clase Coches
coche1 = Coches('blanco', 'VW', 220)
coche2 = Coches('rojo', 'BMW', 250)

print(f"El coche 1 es de color: {coche1.get_color()}")
print(f"El coche 2 es de marca: {coche2.get_marca()}")
print(f"Velocidad de coche1 tras acelerar: {coche1.acelerar(30)} km/h")
print(f"Velocidad de coche1 tras frenar: {coche1.frenar(15)} km/h")
print(coche1.toca_claxon())



