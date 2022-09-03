class Asignatura:

    def __init__(self, nombre, salon="remoto"):
        self.nombre = nombre
        self.salon = salon
    
    def __str__(self):
        return str(self.nombre)+" "+str(self.salon)