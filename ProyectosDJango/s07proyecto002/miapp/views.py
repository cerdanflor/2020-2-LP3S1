from django.shortcuts import render, HttpResponse

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
            <a href="/rango2/10/20">Mostrar Numeros [a,b] (Con Parámetro)</a>
        </li>
    </ul>
    <hr/>
"""

def index(request):
    mensaje =   """
                    <h1> Inicio </h1>
                """
    return HttpResponse(layout + mensaje)

def saludo(request):
    mensaje = """
            <h1>Bienvenidos a la Untels</h1> 
            <h2>Facultad de Ingenieria</h2> 
            <h3>EP Ingenieria de Sistemas</h3> 
            <h4>LP3 - Flor Cerdan</h4>
            """
    return HttpResponse(layout + mensaje)

def rango(request):
    a = 10
    b = 20
    resultado = f"""
        <h2> Número de [{a},{b}] </h2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1

    resultado += "</ul>"
    return HttpResponse(layout + resultado)

def rango2(request,a,b):
    resultado = f"""
        <h2> Rango con parámetros </h2>
        <h2> Número de [{a},{b}] </h2>
        Resultado: <br>
        <ul>
    """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1

    resultado += "</ul>"
    return HttpResponse(layout + resultado)