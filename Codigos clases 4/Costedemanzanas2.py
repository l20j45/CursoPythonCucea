# !!RECUERDA SIEMPRE CASTEAR AL INICIO¡¡¡

#programa que saca el total a pagar de manzanas
Descuento=0
manzanasVendidas =  int(input("Ingresa el numero de manzanas vendidas: "))
manzanasVendidas =  int(manzanasVendidas)
costeDeManzanas  =  float(input("Ingresa el costo por manzanas: "))
#operacion para extraer el total de las manzanas
if manzanasVendidas>=10:
    Descuento=(manzanasVendidas*costeDeManzanas)*.10
    print ("el descuento fue de :", Descuento)
total = (manzanasVendidas*costeDeManzanas)-Descuento
print (total)
#imprime el total