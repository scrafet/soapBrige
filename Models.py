class Afiliado:
    def __init__(self, id_error, resultado, tipo_documento, nro_documento,
                 ape_paterno, ape_materno, nombres,
                 fec_afiliacion, eess, desc_eess, eess_ubigeo,
                 desc_eess_ubigeo, regimen, tipo_seguro, desc_tipo_seguro,
                 contrato, fec_caducidad, estado, tabla, id_num_reg,
                 genero, fec_nacimiento, id_ubigeo, disa,
                 tipo_formato, nro_contrato, correlativo, id_plan,
                 id_grupo_poblacional, msg_confidencial):
        self.id_error = id_error
        self.resultado = resultado
        self.tipo_documento = tipo_documento
        self.nro_documento = nro_documento
        self.ape_paterno = ape_paterno
        self.ape_materno = ape_materno
        self.nombres = nombres
        self.fec_afiliacion = fec_afiliacion
        self.eess = eess
        self.desc_eess = desc_eess
        self.eess_ubigeo = eess_ubigeo
        self.desc_eess_ubigeo = desc_eess_ubigeo
        self.regimen = regimen
        self.tipo_seguro = tipo_seguro
        self.desc_tipo_seguro = desc_tipo_seguro
        self.contrato = contrato
        self.fec_caducidad = fec_caducidad
        self.estado = estado
        self.tabla = tabla
        self.id_num_reg = id_num_reg
        self.genero = genero
        self.fec_nacimiento = fec_nacimiento
        self.id_ubigeo = id_ubigeo
        self.disa = disa
        self.tipo_formato = tipo_formato
        self.nro_contrato = nro_contrato
        self.correlativo = correlativo
        self.id_plan = id_plan
        self.id_grupo_poblacional = id_grupo_poblacional
        self.msg_confidencial = msg_confidencial

    def imprimir(self):
        print("Afiliado:")
        print("id_error:", self.id_error)
        print("resultado:", self.resultado)
        print("tipo_documento:", self.tipo_documento)
        print("nro_documento:", self.nro_documento)
        print("ape_paterno:", self.ape_paterno)
        print("ape_materno:", self.ape_materno)
        print("nombres:", self.nombres)
        print("fec_afiliacion:", self.fec_afiliacion)
        print("eess:", self.eess)
        print("desc_eess:", self.desc_eess)
        print("eess_ubigeo:", self.eess_ubigeo)
        print("desc_eess_ubigeo:", self.desc_eess_ubigeo)
        print("regimen:", self.regimen)
        print("tipo_seguro:", self.tipo_seguro)
        print("desc_tipo_seguro:", self.desc_tipo_seguro)
        print("contrato:", self.contrato)
        print("fec_caducidad:", self.fec_caducidad)
        print("estado:", self.estado)
        print("tabla:", self.tabla)
        print("id_num_reg:", self.id_num_reg)
        print("genero:", self.genero)
        print("fec_nacimiento:", self.fec_nacimiento)
        print("id_ubigeo:", self.id_ubigeo)
        print("disa:", self.disa)
        print("tipo_formato:", self.tipo_formato)
        print("nro_contrato:", self.nro_contrato)
        print("correlativo:", self.correlativo)
        print("id_plan:", self.id_plan)

    def __str__(self):
        return f"Afiliado: {self.nro_documento} - {self.nombres} {self.ape_paterno}"

    def __repr__(self):
        return f"Afiliado({self.id_error}, {self.resultado}, {self.tipo_documento}, {self.nro_documento}, {self.ape_paterno}, {self.ape_materno}, {self.nombres}, {self.fec_afiliacion}, {self.eess}, {self.desc_eess}, {self.eess_ubigeo}, {self.desc_eess_ubigeo}, {self.regimen}, {self.tipo_seguro}, {self.desc_tipo_seguro}, {self.contrato}, {self.fec_caducidad}, {self.estado}, {self.tabla}, {self.id_num_reg}, {self.genero}, {self.fec_nacimiento}, {self.id_ubigeo}, {self.disa}, {self.tipo_formato}, {self.nro_contrato}, {self.correlativo}, {self.id_plan}, {self.id_grupo_poblacional}, {self.msg_confidencial})"

    def eq(self, other):
        return self.nro_documento == other.nro_documento

    def ne(self, other):
        return self.nro_documento != other.nro_documento

    def lt(self, other):
        return self.nro_documento < other.nro_documento

    def le(self, other):
        return self.nro_documento <= other.nro_documento

    def gt(self, other):
        return self.nro_documento > other.nro_documento

    def ge(self, other):
        return self.nro_documento >= other.nro_document
