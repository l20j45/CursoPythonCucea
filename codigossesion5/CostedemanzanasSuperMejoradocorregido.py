from os import system

def saludo():
20    system("clear")
21    print("-------------------------------")
22    print("hola miguel")

def CalculadescuentosManzanas(Vendidas,Coste):
6    if Vendidas==18:
7        Descuento=(Vendidas*coste)*.50
8        print ("Descuento secreto", Descuento)
9    elif Vendidas>=10:
10        Descuento=(manzanasVendidas*coste)*.10
11        print ("Descuento: ",Descuento)
12    else:
13        Descuento=0
14        print ("Sin descuento")
15    total = (Vendidas*coste)-Descuento
    #operacion para extraer el total de las manzanas
16    print (str(total))
17    #imprime el total
    
        #!!RECUERDA SIEMPRE CASTEAR AL INICIO¡¡¡
        #programa que saca el total a pagar de manzanas
1        manzanasVendidas = 1

2        manzanasVendidas = int(input("Ingresa el numero de manzanas vendidas:"))
3  25       while manzanasVendidas!=0:
4            costeDeManzanas = float(input("Ingresa el costo por manzanas: "))
            
5            CalculadescuentosManzanas(manzanasVendidas,costeDeManzanas)

18            esperar=input("")
19           saludo()
23            print("(si ingresas 0 termina el programa)")
24           manzanasVendidas = int(input("Ingresa el numero de manzanas vendidas: "))

26        print("saliendo del programa")