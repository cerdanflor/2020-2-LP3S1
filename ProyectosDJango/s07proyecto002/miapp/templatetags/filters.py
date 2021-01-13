from django import template

register = template.Library()

@register.filter(name='saludo')
def saludo(valor):
    return f"<h1 style='background:green; color:white;'> Bienvenido, {valor} </h1>"