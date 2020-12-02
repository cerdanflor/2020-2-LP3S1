# Insertar varios archivos a bdbiblioteca
import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")

cursor = conexion.cursor()
lista_autores = [('Flor Cerdán','25/10/1978','A'),
                 ('Daniel Lévano','17/01/1978','A'),
                 ('Omar Peña','15/10/1978','A'),
                 ('César Zapata','15/10/1960','A')                 
                ]

lista_editoriales=[('EIU','A'),
                   ('Macro','A'),
                   ('Lima Sur','A'),
                   ('Pirámide','A'),
                   ('Colombus','A'),
                   ('Centro','A')
                   ]
lista_paises = [('Brasil','A'),
                ('Argentina','A'),
                ('Colombia','A'),
                ('Venezuela','A'),
                ('Uruguay','A'),
                ('Paraguay','A'),
                ('USA','A')                
                ]

lista_libros = [('Oracle',10,2019,50,'A',1,1,1),
                ('Sistemas Operativos',14,2016,59,'A',1,4,3),
                ('Estructuras Discretas',6,2018,20,'A',2,2,3),
                ('Algoritmos con Python',8,2017,70,'A',2,2,1),
                ('Power BI',6,1998,50,'A',1,4,2),
                ('Ing. de Software',9,2000,56,'A',3,2,4),
                ('Organización de Computadoras',9,2016,60,'A',7,2,1),
                ('Machine Learning',9,2020,50,'A',4,4,3)
                ]

consulta_pais = """ INSERT INTO PAIS(NOMBRE, ESTADO)
                    VALUES(?,?)
                """
consulta_editorial = """ INSERT INTO EDITORIAL(NOMBRE, ESTADO)
                         VALUES(?,?)
                    """
consulta_autor = """ INSERT INTO AUTOR(NOMBRE, F_NACIMIENTO, ESTADO)
                    VALUES(?,?,?)
                """
consulta_libro = """ INSERT INTO LIBRO(
                        TITULO ,
                        CANTIDAD ,
                        ANIO ,
                        PRECIO ,
                        ESTADO ,
                        IDPAIS ,
                        IDEDITORIAL ,
                        IDAUTOR )
                    VALUES(?,?,?,?,?,?,?,?)
                """
cursor.executemany(consulta_pais, lista_paises)
cursor.executemany(consulta_editorial, lista_editoriales)
cursor.executemany(consulta_autor, lista_autores)
cursor.executemany(consulta_libro, lista_libros)

conexion.commit()

conexion.close()

