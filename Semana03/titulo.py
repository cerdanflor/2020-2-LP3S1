# -*- coding: utf-8 -*-
import camelcase
nombre = "flor elizabeth cerdán león"
print(nombre.upper())
print(nombre.title())

cam = camelcase.CamelCase()
print("Con camelcase...")

print(cam.hump(nombre))
cam2 = camelcase.CamelCase('flor','león')
print(cam2.hump(nombre))


