class maestro:

    def __init__(self, nombre):
        self._nombre = nombre
        self._edad = None
        self._sueldo = None
    
    @property    
    def edad(self):
        return self._edad   

    @property 
    def nombre(self):
        return self._nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def calculosueldo(self, horas):
        pagoporhora=80
        return pagoporhora*horas

class asignatura(maestro):
    def calculosueldo(self, horas):
        pagoporhora=80
        return pagoporhora*horas

class tiempocompleto(maestro):
    def calculosueldo(self, horas):
        pagoporhora=120
        return pagoporhora*horas

class maestros_investigador(maestro):
    def calculosueldo(self, horas):
        pagoporhora=250
        return pagoporhora*horas

       