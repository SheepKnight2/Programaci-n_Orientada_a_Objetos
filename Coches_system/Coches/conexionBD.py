try:
    import mysql.connector
except ImportError:
    print("Debe instalar la librería 'mysql-connector-python' con: pip install mysql-connector-python")
    mysql = None
else:
    try:
        conexion = mysql.connector.connect(
            host='127.0.0.1',
            user="root",
            password="",
            database="bd_coches"
        )
        cursor = conexion.cursor(buffered=True)
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")