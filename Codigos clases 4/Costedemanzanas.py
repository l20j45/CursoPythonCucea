
#!!RECUERDA SIEMPRE CASTEAR AL INICIO¡¡¡

#programa que saca el total a pagar de manzanas
Descuento=0
manzanasVendidas = int(input("Ingresa el numero de manzanas vendidas: "))
costeDeManzanas = float(input("Ingresa el costo por manzanas: "))
if manzanasVendidas>=10:
    Descuento=(manzanasVendidas*costeDeManzanas)*.10
    print ("Descuento: ",Descuento)
total = (manzanasVendidas*costeDeManzanas)-Descuento
#operacion para extraer el total de las manzanas
print (str(total))
#imprime el total
