class Estudiante :    
    def __init__(self, nombre, grado):
            self._nombre = nombre
            self._grado = grado
            self._generacion = 2021
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def grado(self):
        return self._grado
    
    @property
    def generacion(self):
        return self._generacion
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre 
    
    
estudiante1 = Estudiante("daniel","8")
print(estudiante1.nombre)
print(estudiante1.grado)
estudiante1.nombre = "luis"
print(estudiante1.nombre)