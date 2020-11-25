# Crear Base de Datos SQLLite

import sqlite3

# Para conectarnos a la BD
conexion = sqlite3.connect("academico.db")

# Cerrar Conexión
conexion.close()