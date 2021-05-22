# variable = int(input("Ingresa un numero: "))

# tabla = range(1,11)

# for numero in tabla :
#     print(numero*variable)



descuento = 0
numero=0
costo=0
cantidad=0
fruta=""
nombre=''
##AREA DE FUNCIONES
def operacion(fruta) :
    costo = int(input("Ingrese el costo de cada " + fruta + ": "))
    cantidad = int(input("Ingrese la cantidad de " + fruta + "s: "))
    return [costo, cantidad]


nombre = input("Hola cual es tu nombre : ")
numero = int(input("Escribe 1 si quieres manzanas, 2 si quieres duraznos y 3 si quieres peras: "))

while numero < 1 or numero > 3 :
    print("Solo puedes escribir un numero entre en 1 y el 3")
    numero = int(input("Escribe 1 si quieres manzanas, 2 si quieres duraznos y 3 si quieres peras: "))

if numero == 1 :
        fruta = "manzana"
elif numero == 2 :
    fruta = "durazno"
elif numero == 3 :
    fruta = "pera"



resultado = operacion(fruta)

costo = resultado[0]
cantidad = resultado[1]



if nombre.upper() == "DANIEL" :
    descuento = (costo*cantidad)
    print("Felicidades, encontraste el descuento secreto")
elif cantidad>=20:
    descuento=(costo*cantidad)*.15
    print("Descuento: " + str(descuento))
elif cantidad>=10:
    descuento=(costo*cantidad)*.10
    print("Descuento: " + str(descuento))
else:
    print("No hay descuento")


Total = (costo*cantidad)-descuento
print("Total a pagar: " + str(Total))