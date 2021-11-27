#CALCULAR EL PROMEDIO DE 10 ALUMNOS
#GUARDAR LOS DIEZ NOMBRES
#Cada uno tiene tres materias
def comprobarSiEsNumero(calificaion1, listaCalificacion1):
    comprobar = str(calificaion1)
    if comprobar.isdigit :
        listaCalificacion1.append(calificaion1)
        
        

alumno = 0
listaNombre = []
listaCalificacion1 = []
listaCalificacion2 = []
listaCalificacion3 = []

contador = 0
while alumno <11:
    nombre = input("Ingresa el nombre del estudiatente") 
    calificaion1 =input("Ingresa la califacion 1 del alumno"+ contador+1)
    calificaion2 =input("Ingresa la califacion 2 del alumno"+ contador+1)
    calificaion3 =input("Ingresa la califacion 3 del alumno"+ contador+1)
    listaNombre.append(nombre)
    listaCalificacion1.append(calificaion1)
    listaCalificacion2.append(calificaion2)
    listaCalificacion3.append(calificaion3)
    contador+=1