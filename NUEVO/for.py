#Ola ke ase

numeroamultiplicar = int(input("ingresa un numero para mostrarte su tabla de multiplicar: "))



tabla = range(1,11)
for numero in tabla:
    print("numero a multiplicar" + numeroamultiplicar+ "*" +numero)
    print("="+numeroamultiplicar*numero)



numero = int(input('Ingrese el numero: '))

for num in range (1,11):
	print(f'{numero} x {num} =  {num*numero}')



#Declaracion de variables
tabla = range(1, 11)
numero = 0
#Solicitud de datos al usuario
numero = int(input("Ingrese el numero que quiere multiplicar: "))

#Parte logica
for i in tabla :
    mult = numero * i
    print(mult)