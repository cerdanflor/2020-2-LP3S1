# -*- coding: utf-8 -*-
igv = 0.18
def obtenerIGVconSubtotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    # subtotal + igv*subtotal
    # subtotal*(1+0.18)
    return subtotal*(1+igv)
# y porque no poner 1.18???
    
def obtenerSubtotalconTotal(total):
    return total/(1+igv)
def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)