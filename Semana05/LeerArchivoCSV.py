
import csv

with open('Global_Mobility_Report.csv',encoding="utf8") as f:
    datos = csv.reader(f, delimiter=',')
    for fila in datos:
        if fila[2]=='Puno':
            print(f"{fila[0]}\t {fila[1]}\t {fila[2]}\t {fila[3]}\t {fila[4]}\t {fila[5]}\t {fila[6]}\t {fila[7]}\t {fila[8]}\t {fila[9]}\t {fila[10]} \t {fila[11]}\t {fila[12]}")