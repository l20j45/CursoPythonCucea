class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property    
    def region(self):
        return self._region
    
    @property    
    def pais(self):
        return self._pais

    @property    
    def identificador(self):
        return self._identificador

    @region.setter
    def region(self, region):
        self._region = region


casilla = CasillaDeVotacion(123,'Mexico')
print(casilla.identificador)
print(casilla.region)
casilla.region ="occidente"
print(casilla.region)
