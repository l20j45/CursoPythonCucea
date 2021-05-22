class maestro:
    
    def __init__(self,codigo,nombre,departamento,antiguedad):
        self._codigo=codigo
        self._nombre=nombre
        self._departamento=departamento
        self._antiguedad=antiguedad
        
    
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
        self._antiguedad = antiguedad
    @departamento.setter
    def departamento(self, departamento):
        self._departamento = departamento
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo    
        
    def calculoSueldo(self,horasTrabajadas,puesto):
        if (puesto.lower() == "asignatura"):
            self.sueldoPorHora = 80
            return self.sueldoPorHora * horasTrabajadas
        elif (puesto.lower() == "tiempocompleto"):
            self.sueldoPorHora = 100
            return self.sueldoPorHora * horasTrabajadas
        elif (puesto.lower() == "investigador"):
            self.sueldoPorHora = 130
            return self.sueldoPorHora * horasTrabajadas
        else:    
            print ("puesto no encontrado")
        
    def calculoSueldoAsignatura(self,horasTrabajadas):
        self.sueldoPorHora = 80
        return self.sueldoPorHora * horasTrabajadas
    
    def calculoSueldoTiempoCompleto(self,horasTrabajadas):
        self.sueldoPorHora = 100
        return self.sueldoPorHora * horasTrabajadas 
    
    def calculoSueldoInvstigador(self,horasTrabajadas):
        self.sueldoPorHora = 130
        return self.sueldoPorHora * horasTrabajadas
    
    def __str__(self):
        cadena= "nombre: " + self.nombre+"codigo: " + str(self.codigo)
        return cadena
    
