# -*- coding: utf-8 -*-


import financieros
subtotal = 800.77
print(f"subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVconSubtotal(subtotal): .2f}")
print(f"Total:{financieros.obtenerTotalconSubtotal(subtotal):.2f}")