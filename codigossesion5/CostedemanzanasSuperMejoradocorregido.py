from os import system

def saludo():
    system("clear")
    print("-------------------------------")
    print("hola miguel")


def CalculadescuentosManzanas(Vendidas,Coste):
    if Vendidas==18:
        Descuento=(Vendidas*coste)*.75
        
        print ("Descuento secreto", Descuento)
    elif Vendidas>=10:
        Descuento=(manzanasVendidas*coste)*.10
        print ("Descuento: ",Descuento)
    else:
        Descuento=0
        print ("Sin descuento")
    total = (Vendidas*coste)-Descuento
    #operacion para extraer el total de las manzanas
    print (str(total))
    #imprime el total
    
        #!!RECUERDA SIEMPRE CASTEAR AL INICIO¡¡¡
        #programa que saca el total a pagar de manzanas
    manzanasVendidas = 1

    manzanasVendidas = int(input("Ingresa el numero de manzanas vendidas:"))
    while manzanasVendidas!=0:
        costeDeManzanas = float(input("Ingresa el costo por manzanas: "))          
        CalculadescuentosManzanas(manzanasVendidas,costeDeManzanas)
        esperar=input("")
        saludo()
        print("(si ingresas 0 termina el programa)")
        manzanasVendidas = int(input("Ingresa el numero de manzanas vendidas: "))

    print("saliendo del programa")