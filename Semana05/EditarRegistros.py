# UPDATE

import sqlite3
# Para conectarnos a la BD
conexion = sqlite3.connect("academico.db")


cursor = conexion.cursor()
consulta = (""" UPDATE PERSONAS
                SET
                EDAD = 30
                WHERE
                NOMBRE = 'Daniel'
                """)
cursor = conexion.cursor()
cursor.execute(consulta)

conexion.commit()
# Cerrar Conexión
conexion.close()

