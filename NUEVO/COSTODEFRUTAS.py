Descuento=0
Costedemanzana=""
Cantidaddemanzana=""
#Definio e inicializo las variables
Nombre = input("Hola, ¿cuál es tu nombre? ")
Costedemanzana = int(input("Ingrese el costo de la manzana: "))
Cantidaddemanzana = int(input("Ingrese la cantidad de manzanas: "))
#Pidos las variables

if Nombre.upper() == "DANIEL" :
    Descuento = (Costedemanzana*Cantidaddemanzana)
    print("Felicidades, encontraste el descuento secreto")
    if Nombre != "DANIEL":
        print("hola")
elif Cantidaddemanzana>=20:
    Descuento=(Costedemanzana*Cantidaddemanzana)*.15
    print("Descuento: ",Descuento)
elif Cantidaddemanzana>=10:
    Descuento=(Costedemanzana*Cantidaddemanzana)*.10
    print("Descuento: ",Descuento)
else:
    print("no hay descuento")

#defino el descuento
Total = (Costedemanzana*Cantidaddemanzana)-Descuento
#calculo el total
print("Total a pagar: ",Total)