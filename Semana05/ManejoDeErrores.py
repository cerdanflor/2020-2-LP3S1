# vamos a gestionar los errores, con try
# Vamos a suponer un operación sencilla

try:
    numerador = float(input("Numerador: "))
    denominador = float(input("Denominador: "))
    resultado = numerador/denominador
    print(f"Resultado: {resultado}")

# También puedo categorizar mis Excepts
except ZeroDivisionError:
    print("No es posible dividir entre CERO")

# Se ejecuta solo cuando se detecte un error dentro del try
# Se ejecutará cuando no se ejecute ningún except categorizado
except:
    print("Hubo un error")

# Cuando no se detectan errores
else:
    print("La división se realizó con éxito")

# Exista o no exista error, siempre se ejecutará al final 
finally:
    print("La operación Terminó")