import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """  SELECT *
                FROM AUTOR
                ORDER BY NOMBRE
            """
cursor = conexion.cursor()
cursor.execute(consulta)
autores = cursor.fetchall()

for autor in autores:
    print(autor)

conexion.close()

