import random

def ingresaNumero():
    numero = int(input("Escribe una numero--->  "))
    return numero
def comparanumero(numero,numeroescogidoporPc):
    adivinado=False
    if numero>numeroescogidoporPc:
        print("escoge un numero mas pequeño")
        adivinado==False
    elif numero<numeroescogidoporPc:
        print("escoge un numero mas grande")
        adivinado==False
    elif numero==numeroescogidoporPc:
        print("numero adivinado")
        adivinado=True
    return adivinado
    

def run():
    NumeroaAdivinar=random.randint(1,100)    
    adivinado=False
    while adivinado==False:
        numero = ingresaNumero()
        adivinado=comparanumero(numero,NumeroaAdivinar)

        
if __name__ == '__main__':
    run()