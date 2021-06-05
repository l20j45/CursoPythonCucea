import time
class maestro:
    
    def __init__(self,codigo,nombre,departamento,antiguedad):
        self._codigo=codigo
        self._nombre=nombre
        self._departamento=departamento
        self._antiguedad=int(antiguedad)
        
    
    @property    
    def codigo(self):
        return self._codigo   

    @property 
    def nombre(self):
        return self._nombre    
    @property    
    def departamento(self):
        return self._departamento   

    @property 
    def antiguedad(self):
        return self._antiguedad

    @antiguedad.setter
    def antiguedad(self, antiguedad):
        self._antiguedad = str(antiguedad)
        
    @departamento.setter
    def departamento(self, departamento):
        self._departamento = departamento
        
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo    
        

    
    def __str__(self):
        cadena= "nombre: " + self.nombre+" codigo: " + str(self.codigo)
        return cadena
    
class asignatura(maestro):
    def calculoSueldo(self,horasTrabajadas):
        return 80 * horasTrabajadas

class tiempoCompleto(maestro):
    def calculoSueldo(self,horasTrabajadas):
        return 100 * horasTrabajadas
class Investigador(maestro):
    def __init__(self,codigo,nombre,departamento,antiguedad,papers):
        super().__init__(codigo,nombre,departamento,antiguedad)
        self._papers = papers
        
    @property
    def papers(self):
        return self._papers
            
    def calculoSueldo(self,horasTrabajadas):
        return 130 * horasTrabajadas
    
    def tiempodetrabajo(self):
        t = time.localtime()
        return t.tm_year - self._antiguedad