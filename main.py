from suds import client

client = client.Client('http://pruebaapp.sis.gob.pe/sisWSAFI/Service.asmx?WSDL')

response = client.service.GetSession('00003543', '123456')

sessionId = response

print(sessionId)

# Obtiene el tipo de consulta
intOpcion = int(input("Ingrese tipo de consulta : "))

# Obtiene el tipo de documento del afiliado.
tipoDocumento = str(input("Ingrese tipo de documento : "))

# Obtiene el número de documento del afiliado.
nroDocumento = str(input("Ingrese el dni : "))

#  número de documento de seguridad.
Dni = "44790320"

# Llama al método ConsultarAfiliadoFuaE.
responseAfiliado = client.service.ConsultarAfiliadoFuaE(intOpcion, sessionId, Dni, tipoDocumento, nroDocumento)

# Obtiene el afiliado de la respuesta.
afiliado = responseAfiliado

# Si el afiliado no existe, se imprime el mensaje de error.
# if afiliado.IdError != 0:
#   print(afiliado.Resultado)
# else:
# Imprime los datos del afiliado.
#   print(afiliado)
# Si el afiliado no existe, se imprime el mensaje de error.
if afiliado is None:
    print(afiliado.Resultado)
else:
    # Imprime los datos del afiliado.
    print(afiliado)
