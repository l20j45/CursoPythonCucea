"""Programa hecho por daniel
el dia de : 18/19/2021
este programa realiza : blablalablabal
"""
import os
import time
def separador():
    print("====================================================")

def saludo():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
    print("hola "+nombre)
    separador()
    


descuento = 0
nombre ="Luis"
saludo()


print("Programa que calcula el costo de las manzanas")
print("total a pagar")
separador()
totalManzanas = int(input("Ingresa el numero de manzanas vendidas: "))

while totalManzanas!=0:
   
    costeManzanas = int(input("Ingresa cuanto se vendieron las manzanas: "))
    separador()
    if totalManzanas == 18:
        descuento = (totalManzanas*costeManzanas)*.20
        print("hubo un descuento del 20%")
    elif totalManzanas >= 10:
        descuento = (totalManzanas*costeManzanas)*.10
        print("hubo un descuento del 10%")
    else:
        print("no hay descuento")
    print("subtotal: "+str((totalManzanas*costeManzanas)))
    print("descuento: "+str(descuento))
    print("coste final: " + str((totalManzanas*costeManzanas)-descuento))
    time.sleep(3)
    saludo()
    totalManzanas = int(input("Ingresa el numero de manzanas vendidas: "))