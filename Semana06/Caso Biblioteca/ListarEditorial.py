import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """  SELECT *
                FROM EDITORIAL
                ORDER BY NOMBRE
            """
cursor = conexion.cursor()
cursor.execute(consulta)
editoriales = cursor.fetchall()

for editorial in editoriales:
    print(editorial)

conexion.close()
