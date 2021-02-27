def conversion(moneda1,moneda2,nombremoneda1,nombremoneda2):
    print("conversion de "+ nombremoneda1+" a "+nombremoneda2) #concatenacion de nombre de monedas
    convertido=moneda1*moneda2 #conversion de monedas
    print("valor :",convertido) #muestra el valor convertido

def menu(opcion):
    if opcion==1:
        nombremoneda1="pesos" #nombre de la moneda 1 
        nombremoneda2="dolares" #nombre de la moneda 2
        monedasaconvertir=float(input("cuantos "+ nombremoneda1+ " deseas convertir: ")) #cuantas voy a convertir
        monedasaconvertir2=20.58 #valor a convertir
        conversion(monedasaconvertir,monedasaconvertir2,nombremoneda1,nombremoneda2) #funcion que llama a la conversion
        espacio=input("") #espacio para que no lo encime
    elif opcion==2:
        nombremoneda1="pesos"
        nombremoneda2="euros"
        monedasaconvertir=float(input("cuantos "+ nombremoneda1+ " deseas convertir: "))
        monedasaconvertir2=24.44
        conversion(monedasaconvertir,monedasaconvertir2,nombremoneda1,nombremoneda2)
        espacio=input("") 
    elif opcion==3:
        codigo
    elif opcion==4:
        codigo
    elif opcion==5:
        codigo
    elif opcion==6:
        codigo
    else :
        print("opcion no valida")

opcion=0
while opcion!=7 :
    print ("1.- dolar")
    print ("2.- peso euro")
    print ("3.- peso a yuan")
    print ("4.- dolar a euro")
    print ("5.- dolar yuan")
    print ("6.- euro a yuan")
    print ("7.- salir")
    opcion=int(input("ingresa que quieres hacer"))
    menu(opcion)
print("programa terminado")