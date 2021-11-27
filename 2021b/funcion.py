def calcularDescuento(totalManzanas,costeManzanas):
    if totalManzanas == 18:
        descuento = (totalManzanas*costeManzanas)*.20
        print("hubo un descuento del 20%")
    elif totalManzanas >= 10:
        descuento = (totalManzanas*costeManzanas)*.07
        print("hubo un descuento del 7%")
    else:
        print("no hay descuento")
        descuento = 0
    return descuento

def modificarNombre(nombre2):
    nombre ="eric"
    return nombre

nombre ="daniel"
print(nombre.upper())
nombre = modificarNombre(nombre)
print(nombre)