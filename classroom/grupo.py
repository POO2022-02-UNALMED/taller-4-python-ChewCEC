
from classroom.asignatura import Asignatura

class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas={}, estudiantes = []):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
    
    def __str__(self):
        return "Grupo de estudiantes: "+str(self._grupo)

    def listadoAsignaturas(self, **kwargs):
        for key in kwargs:
            self._asignaturas[key] = kwargs[key]

    def agregarAlumno(self, alumno, lista = None):
        if(lista is None):
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista
        
    
    @ classmethod
    def asignarNombre(cls, nombre = "Grado 6"):
        cls.grado = nombre
