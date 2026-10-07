#Programa principal desde la que se manda llamar los objetos de la clase de coches

from coches import Coches, Camiones, Camionetas

coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul","2020",180,150,6)

camion1=Camiones("Dina","Negra",2020, 180, 300, 12,8 ,2500)
camion2=Camiones("Star","Blanco",2016, 150, 200, 14,6 ,2000)

camioneta1=Camionetas("Renault","Amarrillo","2025",240,250,8,"Delantera", True)
camioneta1=Camionetas("Nissan","Blanca","2020", 180, 150,6 ,"Tracera", False)

coche1.acelerar()
coche2.acelerar()

#print(coche1.__velocidad)
print((coche1.getVelocidad))
print((coche2.getVelocidad))
#print(coche1.velocidad)




