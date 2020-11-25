# INSERT VARIOS REGISTROS

import sqlite3
# Para conectarnos a la BD
conexion = sqlite3.connect("academico.db")

# Para crear Tablas en la BD Academico.db
cursor = conexion.cursor()

lista_personas = [('Pablo','Levano',18),
                  ('Daniel','Escalante',20),
                  ('Cristhian','Chipana',22),
                  ('Gerardo','Castillo',18),
                  ('Francisco','Ocaña',15),
                  ('Bryan','Colan',28),
                  ('Anthony','Bendezú',19)                
                ]

cursor.executemany("INSERT INTO PERSONAS VALUES(?,?,?)",lista_personas)
conexion.commit()
# Cerrar Conexión
conexion.close()