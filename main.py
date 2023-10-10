from suds import client

import Models

client = client.Client('http://pruebaapp.sis.gob.pe/sisWSAFI/Service.asmx?WSDL')

response = client.service.GetSession('00003543', '123456')

sessionId = response

print(sessionId)

# Obtiene el tipo de consulta
# intOpcion = int(input("Ingrese tipo de consulta : "))

#  número de documento de seguridad.
Dni = "44790320"

try:
    # Obtiene el tipo de consulta
    intOpcion = int(input("Ingrese tipo de consulta : "))

    if intOpcion == 1:

        # Obtiene el tipo de documento del afiliado.
        tipoDocumento = str(input("Ingrese tipo de documento : "))

        # Obtiene el número de documento del afiliado.
        nroDocumento = str(input("Ingrese el numero de documento : "))

        # Llama al método ConsultarAfiliadoFuaE.
        responseAfiliado = client.service.ConsultarAfiliadoFuaE(intOpcion, sessionId, Dni, tipoDocumento, nroDocumento)

    elif intOpcion == 2:

        # Obtiene el número de contrato del afiliado.
        nroContrato = str(input("Ingrese el Numero de contrato : "))

        # Llama al método ConsultarAfiliadoFuaE.
        responseAfiliado = client.service.ConsultarAfiliadoFuaE(intOpcion, sessionId, Dni, nroContrato)

except ValueError:
    print("El valor introducido no es aceptado")

# Obtiene el afiliado de la respuesta.
afiliado = Models.Afiliado

afiliado.id_error = responseAfiliado.IdError
afiliado.resultado = responseAfiliado.Resultado
afiliado.tipo_documento = responseAfiliado.TipoDocumento
afiliado.nro_documento = responseAfiliado.NroDocumento
afiliado.ape_paterno = responseAfiliado.ApePaterno
afiliado.ape_materno = responseAfiliado.ApeMaterno
afiliado.nombres = responseAfiliado.Nombres
afiliado.fec_afiliacion = responseAfiliado.FecAfiliacion
afiliado.eess = responseAfiliado.EESS
afiliado.desc_eess = responseAfiliado.DescEESS
afiliado.eess_ubigeo = responseAfiliado.EESSUbigeo
afiliado.desc_eess_ubigeo = responseAfiliado.DescEESSUbigeo
afiliado.regimen = responseAfiliado.Regimen
afiliado.tipo_seguro = responseAfiliado.TipoSeguro
afiliado.desc_tipo_seguro = responseAfiliado.DescTipoSeguro
afiliado.contrato = responseAfiliado.Contrato
afiliado.fec_caducidad = responseAfiliado.FecCaducidad
afiliado.estado = responseAfiliado.Estado
afiliado.tabla = responseAfiliado.Tabla
afiliado.id_num_reg = responseAfiliado.IdNumReg
afiliado.genero = responseAfiliado.Genero
afiliado.fec_nacimiento = responseAfiliado.FecNacimiento
afiliado.id_ubigeo = responseAfiliado.IdUbigeo
afiliado.disa = responseAfiliado.Disa
afiliado.tipo_formato = responseAfiliado.TipoFormato
afiliado.nro_contrato = responseAfiliado.NroContrato
afiliado.correlativo = responseAfiliado.Correlativo
afiliado.id_plan = responseAfiliado.IdPlan
afiliado.id_grupo_poblacional = responseAfiliado.IdGrupoPoblacional
afiliado.msg_confidencial = responseAfiliado.MsgConfidencial

try:

    if afiliado.nro_contrato is not None:

        # imprimir afiliado   -- aqui agregar el codigo para ejecutar el SP
        Models.Afiliado.imprimir(afiliado)

    else:

        # imprimir el error
        print(afiliado.resultado)

except ValueError:
    print("El valor del error no es un número")

# Str
# print(afiliado.imprimir())

# repr
# print(repr(afiliado))

# https://www.mytecbits.com/internet/python/execute-sql-server-stored-procedure
