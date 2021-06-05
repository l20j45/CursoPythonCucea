import time

class timer:
    def __init__(self, agnio,mes,dia):
        self.agnio = agnio
        self.mes = mes
        self.dia = dia
    
    @classmethod
    def hoy(cls):
        t = time.localtime()
 
        return cls(t.tm_year, t.tm_mon, t.tm_mday)
 
    def __str__(self):
        return '{}/{}/{}'.format(self.dia, self.mes, self.agnio)
 
    fecha1 = timer(2019,2,21)
    fecha2 = timer.hoy()
    print (fecha1)
    print (fecha2)