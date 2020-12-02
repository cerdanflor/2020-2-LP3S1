import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """  SELECT *
                FROM LIBRO
                ORDER BY CANTIDAD
            """
cursor = conexion.cursor()
cursor.execute(consulta)
libros = cursor.fetchall()

for libro in libros:
    print(libro)

conexion.close()
