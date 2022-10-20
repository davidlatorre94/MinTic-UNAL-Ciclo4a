from repositorios.RepositorioEstudiante import RepositorioEstudiante
from modelos.ModeloEstudiante import ModeloEstudiante


class ControladorEstudiante():

    def __init__(self):
        print("Entró al constructor de la clase ControladorEstudiante")
        self.repositorioEstudiante = RepositorioEstudiante()

    def crearEstudiante(self, bodyRequest):
        print("Creando el estudiante....")
        nuevoEstudiante = ModeloEstudiante(bodyRequest)
        print("estudiante a crear en base de datos: ", nuevoEstudiante.__dict__)
        self.repositorioEstudiante.save(nuevoEstudiante)
        return True

    def buscarEstudiante(self, idObject):
        print("Buscando el estudiante....", idObject)
        estudiante = ModeloEstudiante(self.repositorioEstudiante.findById(idObject))
        return estudiante.__dict__

    def buscarTodosLosEstudiantes(self):
        print("Buscando todos los estudiantes en base de datos....")
        return self.repositorioEstudiante.findAll()

    def actualizarEstudiante(self, estudiante):
        estudianteActual = ModeloEstudiante(self.repositorioEstudiante.findById(estudiante["idObject"]))
        print("Actualizando el estudiante....", estudianteActual)
        estudianteActual.nombre = estudiante["nombre"]
        estudianteActual.apellido = estudiante["apellido"]
        estudianteActual.cedula = estudiante["cedula"]
        self.repositorioEstudiante.save(estudianteActual)
        return True

    def eliminarEstudiante(self, idObject):
        print("Eliminando el estudiante....", idObject)
        self.repositorioEstudiante.delete(idObject)
        return True