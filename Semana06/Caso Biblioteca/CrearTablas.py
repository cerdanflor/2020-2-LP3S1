# Crear Tablas
import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")

tabla_pais =    """ CREATE TABLE PAIS(
                    IDPAIS INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE TEXT UNIQUE,
                    ESTADO TEXT
                )                
                """

tabla_editorial = """ CREATE TABLE EDITORIAL(
                    IDEDITORIAL INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE TEXT UNIQUE,
                    ESTADO TEXT
                )                
                """

tabla_autor =    """ CREATE TABLE AUTOR(
                    IDAUTOR INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE TEXT UNIQUE,
                    F_NACIMIENTO TEXT,
                    ESTADO TEXT
                )                
                """

tabla_libro =    """ CREATE TABLE LIBRO(
                    IDLIBRO INTEGER PRIMARY KEY AUTOINCREMENT,
                    TITULO TEXT,
                    CANTIDAD INTEGER,
                    ANIO INTEGER,
                    PRECIO REAL,
                    ESTADO TEXT,
                    IDPAIS INTEGER REFERENCES PAIS,
                    IDEDITORIAL INTEGER REFERENCES EDITORIAL,
                    IDAUTOR INTEGER REFERENCES AUTOR
                )                
                """
cursor = conexion.cursor()
cursor.execute(tabla_pais)
cursor.execute(tabla_editorial)
cursor.execute(tabla_autor)
cursor.execute(tabla_libro)

conexion.close()


