
# pesos = float(input("cuantos pesos tiene?"))
# valor_de_dollar = float(3875)
# dollares =  pesos / valor_de_dollar
# dollares = round (dollares,2)
# dollares = str(dollares)
# print ("Tienes $"+dollares+" dolares")
dineroInicial= float(input("cuanto dinero quieres convertir? :"))
opcion= int(input(''' que moneda es esta
1 pesos mexicanos
2 pesos argentinos
3 soles
4 canada
'''))
if opcion==1:
    valor_conversion=float(21.4)
    pesos="pesos mexicanos"
elif opcion==2:
    valor_conversion=float(28.4)
    pesos="pesos argentinos"
elif opcion==3:
    valor_conversion=float(25.4)
    pesos="soles"
elif opcion==4:
    valor_conversion=float(26.4)
    pesos="canada"
else : 
    print ("valor no encontrado")
dolares=dineroInicial*valor_conversion
dolares = round(dolares,2)
print ("monto ingresado $"+str(dineroInicial)+" "+ str(pesos))
print ("convertido $"+str(dolares) +" dolares")


