#Parte logica
def inventario() :
    
    inv = ["Mango", "Pera", "Manzana"]
    inv_str = str(inv)[1:-1]
    
    print("\nEl dia de hoy contamos con:\n", inv_str, "\n")

def compra() :
    
    #Declaracion de variables
    cantidad_fruta = 0
    fruta = ""
    nombre = ""
    
    #Solicitud de datos al usuario
    nombre = input("Cual es tu nombre?: ")
    fruta = input("Que fruta compraras?: ")
    cantidad_fruta = int(input("Cual es la cantidad a comprar?: "))
    
    #Eleccion de fruta
    if fruta.strip().casefold() == "pera" :
        calcular_total(15, cantidad_fruta, nombre)
        
    elif fruta.strip().casefold() == "mango" :
        calcular_total(25, cantidad_fruta, nombre)
        
    elif fruta.strip().casefold() == "manzana" :
        calcular_total(10, cantidad_fruta, nombre)
        
    else :
        print("\nfruta no disponible.")
        

def calcular_total(costo_fruta, cantidad_fruta, nombre) :
    
    #Declaracion de variables
    desc = 0
    total = 0
    
    #Decision de descuento
    if nombre.strip().casefold() == "daniel" :
        print("\n¡Felicidades, encontraste el descuento oculto!")
        desc = (costo_fruta * cantidad_fruta)
        
    elif cantidad_fruta >= 10 :
        desc = (costo_fruta * cantidad_fruta) * .10
        print("\nDescuento: ", desc)
        
    else :
        print("\nNo hay descuento.")
    
    total = (costo_fruta * cantidad_fruta) - desc
    print(nombre, ", el total a pagar es: $", total, "\n")

#Salida a consola

print("*****************************")
print("*Bienvenido a la fruteria.py*")
print("*****************************")


inventario()
compra()