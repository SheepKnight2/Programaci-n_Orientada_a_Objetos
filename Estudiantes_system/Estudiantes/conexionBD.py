import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password="",
        database="bd_estudiantes"
        )
    cursor = conexion.cursor(buffered=True)
except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: ")