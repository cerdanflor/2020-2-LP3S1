import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """  SELECT 
                    L.TITULO,
                    A.NOMBRE,
                    P.NOMBRE,
                    E.NOMBRE
                FROM 
                    LIBRO AS L, 
                    AUTOR AS A, 
                    PAIS AS P, 
                    EDITORIAL AS E
                WHERE
                    A.IDAUTOR = L.IDAUTOR AND
                    E.IDEDITORIAL = L.IDEDITORIAL AND
                    P.IDPAIS = L.IDPAIS
                ORDER BY L.TITULO
            """
cursor = conexion.cursor()
cursor.execute(consulta)
libros = cursor.fetchall()

for libro in libros:
    print(libro)

conexion.close()