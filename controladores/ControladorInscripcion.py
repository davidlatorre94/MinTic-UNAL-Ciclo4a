from modelos.ModeloInscripcion import ModeloInscripcion


class ControladorInscripcion():

    def __init__(self):
        print("Entró al constructor de la clase ControladorInscripcion")

    def crearInscripcion(self, bodyRequest):
        print("Creando la inscripcion....")
        inscripcion = ModeloInscripcion(bodyRequest)
        print("inscripcion a crear en base de datos: ", inscripcion.__dict__)
        return True

    def buscarInscripcion(self, idInscripcion):
        print("Buscando la inscripcion....", idInscripcion)
        return True

    def actualizarInscripcion(self, inscripcion):
        print("Actualizando la inscripcion....", inscripcion)
        return True

    def eliminarInscripcion(self, idInscripcion):
        print("Eliminando la inscripcion....", idInscripcion)
        return True