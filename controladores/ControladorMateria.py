from modelos.ModeloMateria import ModeloMateria


class ControladorMateria():

    def __init__(self):
        print("Entró al constructor de la clase ControladorMateria")

    def crearMateria(self, bodyRequest):
        print("Creando la materia....")
        materia = ModeloMateria(bodyRequest)
        print("materia a crear en base de datos: ", materia.__dict__)
        return True

    def buscarMateria(self, idMateria):
        print("Buscando la materia....", idMateria)
        return True

    def actualizarMateria(self, materia):
        print("Actualizando la materia....", materia)
        return True

    def eliminarMateria(self, idMateria):
        print("Eliminando la materia....", idMateria)
        return True