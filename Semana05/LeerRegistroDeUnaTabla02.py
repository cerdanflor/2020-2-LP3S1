
import sqlite3
# Para conectarnos a la BD
conexion = sqlite3.connect("academico.db")

cursor = conexion.cursor()
cursor.execute(""" SELECT *
                   FROM PERSONAS
                   WHERE
                   EDAD >= 20
                   ORDER BY APELLIDO
                """)
# Todo el resultado del select está en Personas
# en java lo conocemos como el ResultSet
personas = cursor.fetchall()

for persona in personas:
    print(persona)

# Cerrar Conexión
conexion.close()
