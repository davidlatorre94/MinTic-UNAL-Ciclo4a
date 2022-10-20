from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from controladores.ControladorDepartamento import ControladorDepartamento
from controladores.ControladorEstudiante import ControladorEstudiante
from controladores.ControladorInscripcion import ControladorInscripcion
from controladores.ControladorMateria import ControladorMateria

controladorDepartamento = ControladorDepartamento()
controladorEstudiante = ControladorEstudiante()
controladorInscripcion = ControladorInscripcion()
controladorMateria = ControladorMateria()

app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


#Registro de endpoints para las funcionalidades de estudiante
@app.route("/estudiante", methods=['POST'])
def crearEstudiante():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorEstudiante.crearEstudiante(requestBody)
    if result:
        return {"resultado": "Estudiante Creado!"}
    else:
        return {"resultado": "Error al crear el Estudiante!"}

@app.route("/estudiante/<string:idObject>", methods=['GET'])
def buscarEstudiante(idObject):
    result = controladorEstudiante.buscarEstudiante(idObject)
    if result is None:
        return {"resultado": "No se encuentra el Estudiante en base de datos!"}
    else:
        return jsonify(result)

@app.route("/estudiante", methods=['GET'])
def buscarTodosLosEstudiantes():
    result = controladorEstudiante.buscarTodosLosEstudiantes()
    if not result:
        return {"resultado": "No se encuentran items en la base de datos!"}
    else:
        return jsonify(result)

@app.route("/estudiante", methods=['PUT'])
def actualizarEstudiante():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorEstudiante.actualizarEstudiante(requestBody)
    if result:
        return {"resultado": "Estudiante actualizado!"}
    else:
        return {"resultado": "Error al actualizar el Estudiante!"}

@app.route("/estudiante/<string:idObject>", methods=['DELETE'])
def eliminarEstudiante(idObject):
    result = controladorEstudiante.eliminarEstudiante(idObject)
    if result:
        return {"resultado": "Estudiante eliminado!"}
    else:
        return {"resultado": "Error al eliminar el Estudiante!"}


#Registro de endpoints para las funcionalidades de departamento
@app.route("/departamento", methods=['POST'])
def crearDepartamento():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorDepartamento.crearDepartamento(requestBody)
    if result:
        return {"resultado": "Departamento Creado!"}
    else:
        return {"resultado": "Error al crear el Departamento!"}

@app.route("/departamento/<string:idDepartamento>", methods=['GET'])
def buscarDepartamento(idDepartamento):
    result = controladorDepartamento.buscarDepartamento(idDepartamento)
    if result is None:
        return {"resultado": "No se encuentra el Departamento en base de datos!"}
    else:
        return jsonify(result)

@app.route("/departamento", methods=['PUT'])
def actualizarDepartamento():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorDepartamento.actualizarDepartamento(requestBody)
    if result:
        return {"resultado": "Departamento actualizado!"}
    else:
        return {"resultado": "Error al actualizar el Departamento!"}

@app.route("/departamento", methods=['DELETE'])
def eliminarDepartamento():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorDepartamento.eliminarDepartamento(requestBody)
    if result:
        return {"resultado": "Departamento eliminado!"}
    else:
        return {"resultado": "Error al eliminar el Departamento!"}


#Registro de endpoints para las funcionalidades de inscripcion
@app.route("/inscripcion", methods=['POST'])
def crearInscripcion():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorInscripcion.crearInscripcion(requestBody)
    if result:
        return {"resultado": "Inscripcion Creado!"}
    else:
        return {"resultado": "Error al crear el Inscripcion!"}

@app.route("/inscripcion/<string:idInscripcion>", methods=['GET'])
def buscarInscripcion(idInscripcion):
    result = controladorInscripcion.buscarInscripcion(idInscripcion)
    if result is None:
        return {"resultado": "No se encuentra el Inscripcion en base de datos!"}
    else:
        return jsonify(result)

@app.route("/inscripcion", methods=['PUT'])
def actualizarInscripcion():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorInscripcion.actualizarInscripcion(requestBody)
    if result:
        return {"resultado": "Inscripcion actualizado!"}
    else:
        return {"resultado": "Error al actualizar el Inscripcion!"}

@app.route("/inscripcion", methods=['DELETE'])
def eliminarInscripcion():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorInscripcion.eliminarInscripcion(requestBody)
    if result:
        return {"resultado": "Inscripcion eliminado!"}
    else:
        return {"resultado": "Error al eliminar el Inscripcion!"}


#Registro de endpoints para las funcionalidades de materia
@app.route("/materia", methods=['POST'])
def crearMateria():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorMateria.crearMateria(requestBody)
    if result:
        return {"resultado": "Materia Creado!"}
    else:
        return {"resultado": "Error al crear el Materia!"}

@app.route("/materia/<string:idMateria>", methods=['GET'])
def buscarMateria(idMateria):
    result = controladorMateria.buscarMateria(idMateria)
    if result is None:
        return {"resultado": "No se encuentra el Materia en base de datos!"}
    else:
        return jsonify(result)

@app.route("/materia", methods=['PUT'])
def actualizarMateria():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorMateria.actualizarMateria(requestBody)
    if result:
        return {"resultado": "Materia actualizado!"}
    else:
        return {"resultado": "Error al actualizar el Materia!"}

@app.route("/materia", methods=['DELETE'])
def eliminarMateria():
    requestBody = request.get_json()
    print("Request body: ", requestBody)
    result = controladorMateria.eliminarMateria(requestBody)
    if result:
        return {"resultado": "Materia eliminado!"}
    else:
        return {"resultado": "Error al eliminar el Materia!"}

#Iniciar servidor
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))

    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
