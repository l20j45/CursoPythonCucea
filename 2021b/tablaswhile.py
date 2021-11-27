contador=0

numero=int(input("Ingresa un numero: "))

while contador <= 100:
    print("tabla del "+str(numero) + "*"+str(contador)  +": "+ str(numero*contador))
    contador = contador + 1