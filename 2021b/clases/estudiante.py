class Estudiante: 
    _nombre=""
    _Apellido_Paterno=""
    _Apellido_Materno=""
    _codigo=""
    _sexo_biologico=""
    _edad=""
    _nacionalidad=""
    _carrera=""
    _estatus_licenciatura=""
    _promedio=""
    _telefono=""
    _correo_electronico=""
    _LinkedIn =""
    _Facebook=""
    _IG=""
    _trabajo=""
    _Colonia=""
    _codigo_Postal=""
    _municipio=""
    _estado=""
    _Pais=""
    
    def __init__(self,nombre,apellidoP,appellidoM,codigo,telefono,email,cp):
        self._nombre=nombre
        self._Apellido_Paterno=apellidoP
        self._Apellido_Materno=appellidoM
        self._codigo=codigo
        self._telefono=telefono
        self._correo_electronico=email
        self._codigo_Postal=cp
    
    #GETTER
            
    @property    
    def codigo(self):
        return self._codigo 

    @property    
    def nombre(self):
        return self._nombre.capitalize()+" "+self._Apellido_Paterno.capitalize()+" "+self._Apellido_Materno.capitalize() 
        
    #Setter
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo 
        
    def registrarmateria():
        pass