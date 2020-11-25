# -*- coding: utf-8 -*-
# Dado el total, calcular el IGV y el subtotal
import financieros
total = 1000.49
print(f"subtotal:{financieros.obtenerSubtotalconTotal(total):.2f}")
print(f"IGV:{financieros.obtenerIGVconTotal(total):.2f}")
print(f"Total:{total}")