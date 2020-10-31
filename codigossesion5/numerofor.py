numeroamultiplicar = int(input("ingresa un numero para mostrarte su tabla de multiplicar: "))
tabla = range(1,11,1)
for contador in tabla:
    print(numeroamultiplicar, contador)
    print(numeroamultiplicar*contador)