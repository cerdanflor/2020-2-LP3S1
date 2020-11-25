# -*- coding: utf-8 -*-
archivo=open("archivo_de_prueba.txt","wt")
contenido = "Línea1 hola amigos como están?\nLínea2 Los estudiantes de LP3 son muy respetuosos, nunca hablan malas palabras."
archivo.write(contenido)
archivo.close()