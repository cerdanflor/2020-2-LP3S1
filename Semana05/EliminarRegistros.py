# DELETE

import sqlite3
# Para conectarnos a la BD
conexion = sqlite3.connect("academico.db")


cursor = conexion.cursor()
consulta = (""" DELETE FROM
                   PERSONAS
                   WHERE
                   EDAD>=22
                """)
cursor = conexion.cursor()
cursor.execute(consulta)

conexion.commit()
# Cerrar Conexión
conexion.close()
