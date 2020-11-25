
import sqlite3
# Para conectarnos a la BD
conexion = sqlite3.connect("academico.db")

# Para crear Tablas en la BD Academico.db
cursor = conexion.cursor()
cursor.execute(""" CREATE TABLE PERSONAS(
                   nombre TEXT, 
                   Apellido TEXT, 
                   edad INTEGER)
                """)

# Cerrar Conexión
conexion.close()
