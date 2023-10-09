from suds import client

client = client.Client('http://pruebaapp.sis.gob.pe/sisWSAFI/Service.asmx?WSDL')

response = client.service.GetSession('00003543', '123456')

sessionId = response

print(sessionId)

# Obtiene el tipo de consulta
intOpcion = input("Ingrese tipo de consulta")

# Obtiene el tipo de documento del afiliado.
tipoDocumento = input("Ingrese tipo de documento")

# Obtiene el número de documento del afiliado.
nroDocumento = input("Ingrese el dni")

#  número de documento de seguridad.
Dni = 44790320

# Llama al método ConsultarAfiliadoFuaE.
responseAfiliado = client.service.ConsultarAfiliadoFuaE(intOpcion, sessionId, Dni, nroDocumento)

# Obtiene el afiliado de la respuesta.
afiliado = responseAfiliado



print('This statement is always executed')


if afiliado.IdError=0:
    # block of code if condition is True
    # Imprime los datos del afiliado.
    print(afiliado)

else:
    # block of code if condition is False
    print(afiliado.Resultado)