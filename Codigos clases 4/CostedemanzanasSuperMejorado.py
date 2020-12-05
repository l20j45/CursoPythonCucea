
#!!RECUERDA SIEMPRE CASTEAR AL INICIO¡¡¡

#programa que saca el total a pagar de manzanas
manzanasVendidas = int(input("Ingresa el numero de manzanas vendidas: "))
costeDeManzanas = float(input("Ingresa el costo por manzanas: "))
if manzanasVendidas>=10:
    Descuento=(manzanasVendidas*costeDeManzanas)*.10
    print ("Descuento: ",Descuento)
elif manzanasVendidas==18:
    Descuento=(manzanasVendidas*costeDeManzanas)*.50
    print ("Descuento secreto", Descuento)
else:
    Descuento=0
    print ("Sin descuento")
total = (manzanasVendidas*costeDeManzanas)-Descuento
#operacion para extraer el total de las manzanas
print (str(total))
#imprime el total