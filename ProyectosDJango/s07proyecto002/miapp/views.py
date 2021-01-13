from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Articulo

# Create your views here.
layout = """
    <h1> Proyecto Web (LP3) || Flor Cerdán </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/saludo">Mensaje de Saludo</a>
        </li>
        <li>
            <a href="/rango">Mostrar Numeros [a,b]</a>
        </li>
        <li>
            <a href="/rango2">Mostrar Numeros [a,b] (Con Parámetro)</a>
        </li>
    </ul>
    <hr/>
"""


def index(request):
    estudiantes = [
        'SERGIO DANIEL VITE COCHACHIN',
        'ANTHONY GERARDO BENDEZU SANTISTEBAN',
        'CRISTIAN ALEXIS CHIPANA HUAMAN',
        'CARLOS GUSTAVO OYOLA SAAVEDRA',
        'GERARDO MANUEL CASTILLO TORDOYA'
    ]
    
    return render(request, 'index.html', {
        'titulo': 'Inicio',
        'mensaje': 'Proyecto Web con DJango',
        'estudiantes': estudiantes
    })


def saludo(request):
    return render(request, 'saludo.html', {
        'titulo': 'Saludo',
        'autor_saludo': 'Mg. Flor Elizabeth Cerdán León'
    })


def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a,b+1)
    return render(request, 'rango.html',{
        'titulo': 'Rango',
        'a':a,
        'b':b,
        'rango_numeros':rango_numeros
    })


def rango2(request, a=0, b=100):
    if a > b:
        return redirect('rango2', a=b, b=a)

    resultado = f"""
        <h2> Rango con parámetros </h2>
        <h2> Número de [{a},{b}] </h2>
        Resultado: <br>
        <ul>
    """
    while a <= b:
        resultado += f"<li> {a} </li>"
        a += 1

    resultado += "</ul>"
    return HttpResponse(layout + resultado)

def crear_articulo(request, titulo, contenido, publicado):
    articulo = Articulo(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    articulo.save()
    return HttpResponse(f"Artículo Creado: {articulo.titulo} - {articulo.contenido}")

def buscar_articulo(request):
    try:
        articulo = Articulo.objects.get(id=2)
        resultado = f"""Articulo: 
                        <br> <strong>ID:</strong> {articulo.id} 
                        <br> <strong>Título:</strong> {articulo.titulo} 
                        <br> <strong>Contenido:</strong> {articulo.contenido}
                        """
    except:
        resultado = "<h1> Artículo No Encontrado </h1>"
    return HttpResponse(resultado)

def editar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)

    articulo.titulo = "Enseñanza onLine en la UNTELS"
    articulo.contenido = "Aula Virtual, Google Meet, Portal Académico, Google Classroom..."
    articulo.publicado = False

    articulo.save()
    return HttpResponse(f"Articulo Editado: {articulo.titulo} - {articulo.contenido}")

def listar_articulos(request):
    articulos = Articulo.objects.order_by('titulo')
    return render(request, 'listar_articulos.html',{
        'articulos': articulos,
        'titulo': 'Listado de Artículos'
    })

def eliminar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.delete()
    return redirect('listar_articulos')