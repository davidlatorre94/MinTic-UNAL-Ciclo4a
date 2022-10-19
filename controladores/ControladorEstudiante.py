from modelos.ModeloEstudiante import ModeloEstudiante


class ControladorEstudiante():

    def __init__(self):
        print("Entró al constructor de la clase ControladorEstudiante")

    def crearEstudiante(self, bodyRequest):
        print("Creando el estudiante....")
        estudiante = ModeloEstudiante(bodyRequest)
        print("estudiante a crear en base de datos: ", estudiante.__dict__)
        return True

    def buscarEstudiante(self, cedula):
        print("Buscando el estudiante....", cedula)
        return True

    def actualizarEstudiante(self, estudiante):
        print("Actualizando el estudiante....", estudiante)
        return True

    def eliminarEstudiante(self, estudiante):
        print("Eliminando el estudiante....", estudiante)
        return True