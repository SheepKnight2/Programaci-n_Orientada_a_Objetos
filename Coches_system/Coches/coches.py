from coches import conexionBD,cursor

print("\033c")

class Coches:
    def __init__(self,marca,color,modelo,velocidad,potencia,asientos):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._potencia=potencia
        self._asientos=asientos

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.Velocidad-=1

    def getVelocidad(self):
        return self._velocidad

    def getmarca(self):
        return self._marca

    def getcolor(self):
        return self._color
    
    def getcolor(self):
        return self._color
    
    def setVelocidad(self, velocidad):
        self._velocidad=velocidad
    
    def setmarca(self,marca):
        self._velocidad=marca
    
    def setcolor(self,color):
        self._color=color

    def getmodelo(self):
        return self.__modelo
    
    def setmodelo(self, modelo):
        self.__modelo=modelo

    def getvelocidad(self):
        return self.__velocidad

    def setvelocida(self,velocidad ):
        self.__velocidad=velocidad

    def getpotencia(self):
        return self.__potencia

    def setpotencia(self, potencia):
        self.__potencia=potencia

    def getasientos(self):
        return self.__asientos

    def getasientos(self, asientos):
        self.__asientos=asientos

    def insertar(self):
        try:
            sql = """
                INSERT INTO coches (marca, color, modelo, velocidad, potencia, asientos) VALUES (%s, %s, %s, %s, %s, %s)
            """

            valores = (
                self._marca,
                self._color,
                self._modelo,
                self._velocidad,
                self._potencia,
                self._asientos
            )

            cursor.execute(sql, valores)
            conexionBD.commit()

            return True

        except Exception as e:
            print("Error al insertar el coche:", e)
            return False

    def consultar(self):
        try:
            cursor.execute("SELECT * FROM coches WHERE marca = %s AND modelo = %s", (self._marca, self._modelo))
            return cursor.fetchone()
        except Exception as e:
            print("Error al consultar el coche:", e)
            return None

    def eliminar(self):
        try: 
            cursor.execute("DELETE FROM coches WHERE marca = %s AND modelo = %s", (self._marca, self._modelo))
            conexionBD.commit()
            return True
        except Exception as e:
            print("Error al eliminar el coche:", e)
            return False

    def actualizar(self):
        try:
            cursor.execute("UPDATE coches SET color = %s, velocidad = %s, potencia = %s, asientos = %s WHERE marca = %s AND modelo = %s",
                           (self._color, self._velocidad, self._potencia, self._asientos, self._marca, self._modelo))
            conexionBD.commit()
            return True
        except Exception as e:
            print("Error al actualizar el coche:", e)
            return False