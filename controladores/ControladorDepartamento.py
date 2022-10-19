from modelos.ModeloDepartamento import ModeloDepartamento


class ControladorDepartamento():

    def __init__(self):
        print("Entró al constructor de la clase ControladorDepartamento")

    def crearDepartamento(self, bodyRequest):
        print("Creando el departamento....")
        departamento = ModeloDepartamento(bodyRequest)
        print("departamento a crear en base de datos: ", departamento.__dict__)
        return True

    def buscarDepartamento(self, idDepartamento):
        print("Buscando el departamento....", idDepartamento)
        return True

    def actualizarDepartamento(self, departamento):
        print("Actualizando el departamento....", departamento)
        return True

    def eliminarDepartamento(self, departamento):
        print("Eliminando el departamento....", departamento)
        return True