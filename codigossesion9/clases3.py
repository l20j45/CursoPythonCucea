class Persona:

    def __init__(self, nombre):
        self.nombre=nombre
        
    @property
    def getNombre(self):
            return self.nombre

    def avanza(self):        
        print('anda caminando')

class Ciclista(Persona):
    def __init__(self,nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print('anda en bicicleta')
 
def  main():
    persona=Persona('JUAN')
    print(f'{persona.getNombre}:') 
    persona.avanza()
    
    Ciclista1=Ciclista('LUIS')
    print(f'{Ciclista1.getNombre}:') 
    Ciclista1.avanza()

    
if __name__ == "__main__":
    main()