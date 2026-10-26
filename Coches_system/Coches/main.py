import coches
import coches

class App:
    def borrarPantalla(self):
        print("\033c")

    def esperarTecla(self):
        input("... ¡Oprima cualquier tecla para continuar!...")

    def terminar(self):
        input("... :::!GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n vuelva pronto! :::...")

    def opcionInvalida(self):
        print("\n\t... ¡Opcion invalida!...")
        self.esperarTecla()

    def menu_acciones(self,tipo):
        print(f"\n\t...::: Menu de {tipo} :::...\n")
        opcion=input("\n\t 1.- Agregar \n\t 2.- Mostrar \n\t 3.- Borrar \n\t 4.- Modificar \n\t 5.- Salir \n\t\t Elegir una opcion: ")
        return opcion

    def respuesta_sql(self,respuesta):
        if respuesta:
            input("\n\t...¡Accion Realizada con Exito...")
        else:
            input("\n\t...¡Esta Accion no pudo realizarse en este momento!...")

    def pedir_numero(self, texto):
        dato = input(texto).strip()
        while not dato.isdigit():
            print("\t... Solo se permiten numeros ...")
            dato = input(texto).strip()
        return dato

    def datos_coche(self, tipo):
        self.borrarPantalla()
        print(f"\n\t...::: Ingresar los datos del {tipo} :::...\n")
        cochesito = {}
        cochesito["marca"] = input("\t Marca: ").upper().strip()
        cochesito["color"] = input("\t Color: ").upper().strip()
        cochesito["modelo"] = input("\t Modelo: ").upper().strip()
        cochesito["velocidad"] = self.pedir_numero("\t Velocidad: ")
        cochesito["potencia"] = self.pedir_numero("\t Potencia: ")
        cochesito["asientos"] = self.pedir_numero("\t # de asientos: ")
        return cochesito

    def menu_coches(self):
        while True:
            self.borrarPantalla()
            opc = self.menu_acciones("Coches")
            match opc:
                case '1':
                    cochesito = self.datos_coche("Coche")
                    coche1 = coches(cochesito['marca'], cochesito['color'], cochesito['modelo'], cochesito['velocidad'], cochesito['potencia'], cochesito['asientos'])
                    coches1 = coches.coches(cochesito['marca'], cochesito['color'], cochesito['modelo'], cochesito['velocidad'], cochesito['potencia'], cochesito['asientos'])
                    respuesta = coches1.insertar()
                    self.respuesta_sql(respuesta)

                case '2':
                    self.borrarPantalla()
                    coches1 = coches.coches('','','',0,0,0)
                    registros = coches1.consultar()
                    num_coche = 1
                    if registros:
                        for fila in registros:
                            print(f"\n\tCoche #: {num_coche}\n\t\tID: {fila[0]}\n\t\tMarca: {fila[1]}\n\t\tColor: {fila[2]}\n\t\tModelo: {fila[3]}\n\t\tVelocidad: {fila[4]}\n\t\tPotencia: {fila[5]}\n\t\tAsientos: {fila[6]}")
                            num_coche+=1
                    else:
                        print("\n\t... No hay coches registrados...")
                    self.esperarTecla()

                case '3':
                    self.borrarPantalla()
                    id_borrar = self.pedir_numero("\t ID a borrar: ")
                    coches1 = coches.coches('','','',0,0,0)
                    respuesta = coches1.borrar(id_borrar)
                    self.respuesta_sql(respuesta)

                case '4':
                    self.borrarPantalla()
                    id_mod = self.pedir_numero("\t ID a modificar: ")
                    cochesito = self.datos_coche("Coche a modificar")
                    coches1 = coches.coches(cochesito['marca'], cochesito['color'], cochesito['modelo'], cochesito['velocidad'], cochesito['potencia'], cochesito['asientos'])
                    respuesta = coches1.modificar(id_mod)
                    self.respuesta_sql(respuesta)

                case '5':
                    break
                case _:
                    self.opcionInvalida()

    def main(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = input("\n\t ::: Menu Principal :::\n\t1.- Coches\n\t2.- Salir\n\tElegir una opcion: ")
            match opcion:
                case "1":
                    self.menu_coches()
                case "2":
                    self.terminar()
                    opcion = False
                case _:
                    self.opcionInvalida()

if __name__ == "__main__":
    app = App()
    app.main()