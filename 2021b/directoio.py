def validaTexto():
    error=True
    nombre =input("Ingresa tu nombre")
    if nombre.isalpha():
        return False, nombre
    else :
        print("dame un nombre de verdad")
        return True

class Estudiante: 
    nombre=""
    sexobiologico=""
    edad=""
    nacionalidad=""
    carrera=""
    estatus_licenciatura=""
    promedio=""
    telefono=""
    correo_electronico=""
    LinkedIn =""
    Facebook=""
    IG=""
    trabajo=""
    Colonia=""
    codigo_Postal=""
    municipio=""
    estado=""
    Pais=""

error = True
nombre = ""
estudiante1 = Estudiante()
estudiante1.nombre="daniel"
print(estudiante1)
print(estudiante1.nombre)
estudiante2 = Estudiante()
while error == True:
    error = validaTexto()
estudiante2.edad=22
estudiante2.nombre=nombre
print(estudiante2.nombre, estudiante2.edad)