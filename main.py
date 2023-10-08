import requests

def get_session(usuario, clave):
    # Crea la solicitud HTTP
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"usuario": usuario, "clave": clave}

    # Realiza la solicitud
    response = requests.post("http://pruebaapp.sis.gob.pe/sisWSAFI/Service.asmx/GetSession", headers=headers, data=data)

    # Verifica el código de respuesta
    if response.status_code == 200:
        # Devuelve la respuesta del servicio
        return response.json()
    else:
        # Imprime el error
        print(response.text)

# Obtiene la respuesta del servicio
response = get_session("00003543", "123456")

# Verifica la respuesta
if response:
    # La respuesta es válida
    print(response["token"])
else:
    # La respuesta no es válida
    print("La respuesta no es válida")
