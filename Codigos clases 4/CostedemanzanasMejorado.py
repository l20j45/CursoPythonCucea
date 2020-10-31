def pedirDatos():
    manzanasVendidas = int(input("Ingresa el numero de manzanas vendidas: "))
    costeDeManzanas = float(input("Ingresa el costo por manzanas: "))

def Calcular():
    if manzanasVendidas==18:
        Descuento=(manzanasVendidas*costeDeManzanas)*.50
        print ("Descuento secreto: ",Descuento)
    elif manzanasVendidas>=10:
        Descuento=(manzanasVendidas*costeDeManzanas)*.10
        print ("Descuento: ",Descuento)
    else:
        Descuento=0
        print ("Sin descuento")


def Mostratotales():
    total = (manzanasVendidas*costeDeManzanas)-Descuento
    print (str(total))

#!!RECUERDA SIEMPRE CASTEAR AL INICIO¡¡¡
manzanasVendidas=0
costeDeManzanas=0
Descuento=0
pedirDatos()
Calcular()
Mostratotales()