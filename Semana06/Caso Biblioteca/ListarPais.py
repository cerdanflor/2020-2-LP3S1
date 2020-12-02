import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """  SELECT *
                FROM PAIS
                ORDER BY NOMBRE
            """
cursor = conexion.cursor()
cursor.execute(consulta)
paises = cursor.fetchall()

for pais in paises:
    print(pais)

conexion.close()