"""
1-Api con python utilizando flask importando las librerías necesarias.
"""
# Importar las librerías necesarias
from flask import Flask, request, jsonify
import requests

"""
2. Configuración inicial
en realidad el id del usuario y los datos del cliente tienen que ser recibidos por un 
login y no grabar esos datos de forma estática en un código.
"""
app = Flask(__name__)

# Aquí se configurará el login para obtener el ID del usuario y los datos del cliente

"""
3. Autenticación
Es necesario implementar una función de autenticación para obtener el token de acceso (Bearer token).
"""
def obtener_token():
	DEFINIR headers = ...
	#dependera tambien de como es el login
    DEFINIR body = {
    	"grant_type": "client_credentials",
    	"client_id": CLIENT_ID,
    	"client_secret": CLIENT_SECRET,
    	"scope": "https://graph.microsoft.com(o algo así)"
	}
    #respuesta para el front de forma de api rest
	DEFINIR response = POST request A TOKEN_URL CON headers Y body
	RETORNAR response.json().get("access_token")

"""
4. Función básica para realizar una petición a Microsoft Graph
Desarrollar una función que realice peticiones a Microsoft Graph para utilizar uno de sus servicios (endpoint de la API).
"""
def obtener_eventos(access_token):
	DEFINIR headers = {
    	"Authorization": concatenar("Bearer ", access_token),
    	"Content-Type": "application/json"
	}
    ##la idea es que sea una funcion que llame a otras funciones que serían los distintos servicion que ofrece microsoft graphic, por eso 
    #lo de /me/events pq son funciones especificas de microsof graphic como crear reunion o lo que sea que seran llamados por esta función
	DEFINIR response = GET request A concatenar(MICROSOFT_GRAPH_URL, "/me/events") CON headers
	RETORNAR response.json()

"""
5. Funciones para cada servicio de Microsoft Graph (Calendar, Mail, etc.)
Desarrollar funciones específicas para cada uno de los servicios.
"""
def obtener_calendario(token):
    return peticion_a_microsoft_graph("me/calendar", token)

def obtener_correos(token):
    return peticion_a_microsoft_graph("me/mail", token)
#lo mismo para crear cada uno de ellos y muchas funciones de este estilo

"""
6. Funciones para crear eventos, entre otros
Desarrollar funciones para realizar acciones específicas, como crear eventos.
"""
#hay que comprobar siempre que el usuario pueda realizar la accion 
def crear_evento(token, evento):
    url = "https://graph.microsoft.com/v1.0/me/events"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=evento)
    return response.json()
    """
7. Función de conexión para definir el endpoint del chatbot
Definir el endpoint para el chatbot en Flask.
"""
ç@app.route('/chatbot', methods=['POST'])
def chatbot_endpoint():
    datos = request.json
    token = obtener_bearer_token()
    # Procesar datos y utilizar funciones específicas según sea necesario
    respuesta = procesar_peticion_chatbot(datos, token)
    return jsonify(respuesta)

def procesar_peticion_chatbot(datos, token):
    #La idea general aqui es Implementar la lógica del chatbot utilizando las funciones desarrolladas
    # (ejemplo: obtener calendario, crear evento, etc.)
    """
	DEFINIR data = request.json
	DEFINIR access_token = obtener_token()
    
	SI data['intention'] ES igual A 'obtener_eventos':
    	DEFINIR eventos = obtener_eventos(access_token)
    	RETORNAR jsonify(eventos)
	SINO SI data['intention'] ES igual A 'crear_evento':
    	DEFINIR evento = data['details']
    	DEFINIR resultado = crear_evento(evento, access_token)
    	RETORNAR jsonify(resultado)
	SINO SI data['intention'] ES igual A 'buscar_documento':
    	DEFINIR nombre_documento = data['nombre_documento']
    	DEFINIR documento = buscar_documento(nombre_documento, access_token)
    	RETORNAR jsonify(documento)
	SINO SI data['intention'] ES igual A 'actualizar_tarea':
    	DEFINIR id_tarea = data['id_tarea']
    	DEFINIR estado = data['estado']
    	DEFINIR resultado = actualizar_tarea(id_tarea, estado)
    	RETORNAR jsonify(resultado)
	SINO:
    	RETORNAR jsonify({"mensaje": "Intención no reconocida"})
    pass
"""
if __name__ == '__main__':
    app.run(debug=True)
""" 
Es bueno tambie definir promps para limitar o controlar mejor dicho el bot como por ejemplo
-"Parece que tienes varias tareas pendientes. ¿Quieres que te ayude a priorizarlas?"
-"Recordatorio: [nombre del evento] está programado para [hora del evento]."
-notificaciones y alertas es importate
-"¿Estás seguro de que quieres [acción]? Por favor, confirma."
"""
