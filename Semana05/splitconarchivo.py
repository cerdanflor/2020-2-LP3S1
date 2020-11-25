
# ¿Es posible pasar el contenido de un archivo a una lista ????
noticia = open("noticia.txt","rt",encoding='utf8')
datos_noticia = noticia.read()

lista = datos_noticia.split()
listaconcriterio = datos_noticia.split('de')



print(f"Texto Original: {datos_noticia}")
print("Noticia en Lista: ")
print(lista)
print(f"\nlista[0]: {lista[0]}")
print(f"lista[1]: {lista[1]}")
print(f"lista[2]: {lista[2]}")
print(f"lista[3]: {lista[3]}")
print(f"lista[4]: {lista[4]}")

print("\nLista con criterio de separacion: ")
print(listaconcriterio)
print(f"\nlistaconcriterio[0]: {listaconcriterio[0]}")
print(f"listaconcriterio[1]: {listaconcriterio[1]}")
print(f"listaconcriterio[2]: {listaconcriterio[2]}")