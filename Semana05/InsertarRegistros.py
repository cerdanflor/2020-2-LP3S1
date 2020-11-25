# INSERT

import sqlite3
# Para conectarnos a la BD
conexion = sqlite3.connect("academico.db")

# Para crear Tablas en la BD Academico.db
cursor = conexion.cursor()
cursor.execute(""" INSERT INTO PERSONAS VALUES(
                    'Sergio',
                    'Vite Cochachin',
                    21                    
                    )             
                """)
conexion.commit()
# Cerrar Conexión
conexion.close()
