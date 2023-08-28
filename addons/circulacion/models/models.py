# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cliente(models.Model):
    _name = "circulacion.cliente"
    _description = "circulacion.cliente"

    name = fields.Char(string="Nombre(s)*", required=True)
    fotografia = fields.Binary(string="Fotografía")
    apellido = fields.Char(string="Apellido(s)*", required=True)
    empresa = fields.Char(string="Nombre de Compañia")
    nit = fields.Char(string="NIT", default="C/F")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    no_documento = fields.Char()
    talla = fields.Char()
    nombre_facturacion = fields.Char(string="Nombre de Facturación*", required=True)
    dir_facturacion = fields.Char(string="Dirección de Facturación*", required=True)
    telefono = fields.Char(string="Teléfonos*", required=True)
    correo = fields.Char(string="Correo Electrónico")
    # precio_unidad = fields.Float(
    #     default=1.66, readonly=True, digits=(16, 2), string="Precio por Unidad"
    # )

    precio_unidad = fields.Float(
        compute="_compute_precio_dias",
        readonly=True,
        store=True,
        digits=(16, 2),
        string="Precio por Unidad*",
    )

    # dias_validos_devolucion = fields.Integer(
    #     default=1, string="Días Válidos para Devolución"
    # )

    dias_validos_devolucion = fields.Integer(
        compute="_compute_precio_dias",
        inverse="_inverse_dias_validos_devolucion",
        store=True,
        string="Días Válidos para Devolución*",
        required=True,
    )

    cantidad_pedido = fields.Integer(
        default=0, string="Cantidad de Pedido Ordinario*", required=True
    )
    cantidad_flete = fields.Integer(
        default=0, string="Cantidad de Flete*", required=True
    )
    cantidad_promocion = fields.Integer(
        default=0, string="Cantidad de Promoción*", required=True
    )
    tipo_documento = fields.Selection(
        [
            ("cedula", "Cedula"),
            ("dpi", "DPI"),
            ("pasaporte", "Pasaporte"),
            ("otros", "Otros"),
        ],
        string="Tipo de Documento",
        default="cedula",
        required=True,
    )
    tipo_persona = fields.Selection(
        [
            ("individual", "Individual"),
            ("juridica", "Jurídica"),
        ],
        string="Tipo de Persona*",
        default="individual",
        required=True,
    )

    talla = fields.Selection(
        [
            ("s", "S"),
            ("m", "M"),
            ("l", "L"),
            ("xl", "XL"),
            ("xxl", "XXL"),
            ("xxxl", "XXXL"),
        ],
        string="Talla*",
        default="s",
        required=True,
    )

    canal_facturacion = fields.Selection(
        [
            ("sectores_metropolitanos", "Sectores Metropolitanos"),
            ("sectores_departamentales", "Sectores Departamentales"),
            ("tiendas_barrio", "Tiendas de Barrio"),
            ("tiendas_conveniencia", "Tiendas de Conveniencia"),
            ("suscripciones", "Suscripciones"),
            ("suscripciones_cortesia", "Suscripciones de Cortesia"),
            ("agencias_publicidad", "Agencias de Publicidad"),
            ("oficinas_zona_12", "Oficinas Zona 12"),
            ("envios_usa", "Envios a USA"),
            ("otros", "Otros"),
        ],
        string="Canales de Facturación*",
        default="sectores_metropolitanos",
        required=True,
    )

    tipo_documento = fields.Selection(
        [
            ("cedula", "Cedula"),
            ("dpi", "DPI"),
            ("pasaporte", "Pasaporte"),
            ("otros", "Otros"),
        ],
        string="Tipo de Documento",
        default="cedula",
    )
    tipo_persona = fields.Selection(
        [
            ("individual", "Individual"),
            ("juridica", "Jurídica"),
        ],
        string="Tipo de Persona",
        default="individual",
        required=True,
    )

    talla = fields.Selection(
        [
            ("s", "S"),
            ("m", "M"),
            ("l", "L"),
            ("xl", "XL"),
            ("xxl", "XXL"),
            ("xxxl", "XXXL"),
        ],
        string="Talla",
        default="s",
    )

    canal_distribucion = fields.Selection(
        [
            ("sectores_metropolitanos", "Sectores Metropolitanos"),
            ("sectores_departamentales", "Sectores Departamentales"),
            ("tiendas_barrio", "Tiendas de Barrio"),
            ("tiendas_conveniencia", "Tiendas de Conveniencia"),
            ("suscripciones", "Suscripciones"),
            ("suscripciones_cortesia", "Suscripciones de Cortesia"),
            ("agencias_publicidad", "Agencias de Publicidad"),
            ("oficinas_zona_12", "Oficinas Zona 12"),
            ("envios_usa", "Envios a USA"),
            ("otros", "Otros"),
        ],
        string="Canales de Distribución*",
        required=True,
    )

    canal_facturacion = fields.Selection(
        [
            ("sectores_metropolitanos", "Sectores Metropolitanos"),
            ("sectores_departamentales", "Sectores Departamentales"),
            ("tiendas_barrio", "Tiendas de Barrio"),
            ("tiendas_conveniencia", "Tiendas de Conveniencia"),
            ("suscripciones", "Suscripciones"),
            ("suscripciones_cortesia", "Suscripciones de Cortesia"),
            ("agencias_publicidad", "Agencias de Publicidad"),
            ("oficinas_zona_12", "Oficinas Zona 12"),
            ("envios_usa", "Envios a USA"),
            ("otros", "Otros"),
        ],
        string="Canales de Facturación*",
        required=True,
    )

    estado = fields.Selection(
        [
            ("Activo", "Activo"),
            ("Inactivo", "Inactivo"),
        ],
        string="Estado*",
        default="Activo",
        required=True,
    )

    facturar_pedidos = fields.Selection(
        [
            ("si", "Si"),
            ("no", "No"),
        ],
        string="Facturar Pedidos*",
        default="si",
        required=True,
    )

    @api.depends("canal_distribucion")
    def _compute_precio_dias(self):
        for record in self:
            if record.canal_distribucion == "sectores_metropolitanos":
                record.precio_unidad = 1.66
                record.dias_validos_devolucion = 5
            elif record.canal_distribucion == "sectores_departamentales":
                record.precio_unidad = 1.71
                record.dias_validos_devolucion = 3
            else:
                record.precio_unidad = 0
                record.dias_validos_devolucion = 0

    def _inverse_dias_validos_devolucion(self):
        pass


class Country(models.Model):
    _name = "circulacion.country"
    name = fields.Char(string="Country Name")


class State(models.Model):
    _name = "circulacion.state"
    name = fields.Char(string="State Name")
    country_id = fields.Many2one("circulacion.country", string="Country")


class City(models.Model):
    _name = "circulacion.city"
    name = fields.Char(string="City Name")
    state_id = fields.Many2one("circulacion.state", string="State")


class Ruta(models.Model):
    _name = "circulacion.ruta"
    name = fields.Char(string="Ruta")
    city_id = fields.Many2one("circulacion.city", string="Ruta")


# Empresa
class Empresa(models.Model):
    _name = "circulacion.empresa"
    name = fields.Char(string="Nombre de la Empresa")


# Publicación
class Publicacion(models.Model):
    _name = "circulacion.publicacion"
    name = fields.Char(string="Nombre de la Publicación")
    empresa_id = fields.Many2one("circulacion.empresa", string="Empresa")


# Tipo de Publicación
class TipoPublicacion(models.Model):
    _name = "circulacion.tipopublicacion"
    name = fields.Char(string="Tipo de Publicación")
    publicacion_id = fields.Many2one("circulacion.publicacion", string="Publicación")


# Tipo de Portada
class TipoPortada(models.Model):
    _name = "circulacion.tipoportada"
    name = fields.Char(string="Tipo de Portada")
    publicacion_id = fields.Many2one("circulacion.publicacion", string="Publicación")


class sector(models.Model):
    _name = "circulacion.sector"
    _description = "circulacion.sector"

    name = fields.Char(string="Nombre del Sector*", required=True, default="Dirección")
    calle_avenida = fields.Char(string="Calle o Avenida*", required=True, default="N/A")
    no_casa = fields.Char(string="No. de Casa*", required=True, default="N/A")
    no_apartamento = fields.Char(
        string="No. de Apartamento*", required=True, default="N/A"
    )
    zona = fields.Char(string="Zona*", required=True, default="N/A")
    colonia_barrio_aldea = fields.Char(
        string="Colonia, Barrio o Aldea*", required=True, default="N/A"
    )
    cliente = fields.Many2one("circulacion.cliente")
    # id_cliente = fields.Integer(
    #     string="ID del Cliente", compute="_compute_cliente_id", readonly=True
    # )
    cliente_info = fields.Char(
        string="Información del Cliente", compute="_compute_cliente_info"
    )

    orden_ruta = fields.Integer(default=1, string="Orden de la Ruta*", required=True)
    tipo_direccion = fields.Selection(
        [
            ("entrega", "Entrega"),
            ("facturacion", "Facturación"),
            ("ambas", "Ambas"),
        ],
        string="Tipo de Direccion*",
        default="ambas",
        required=True,
    )

    # Configuracion
    tasa_devolucion = fields.Integer(string="Tasa de Devolución *", required=True)
    dias_valido_devolucion = fields.Integer(
        string="Días Válidos para Devolución *", required=True
    )
    cantidad_pedido_ordinario = fields.Integer(
        string="Cantidad de Pedido Ordinario *", required=True
    )
    cantidad_flete = fields.Integer(string="Cantidad de Flete *", required=True)
    cantidad_promocion = fields.Integer(string="Cantidad de Promoción *", required=True)
    supervisor = fields.Many2one("circulacion.supervisor")
    transportista = fields.Many2one("circulacion.transportista")
    cobrador = fields.Many2one("circulacion.cobrador", required=True)

    # Campos para Paises
    country_id = fields.Many2one("circulacion.country", string="Pais*", required=True)
    state_id = fields.Many2one(
        "circulacion.state", string="Departamento*", required=True
    )
    city_id = fields.Many2one("circulacion.city", string="Municipio*", required=True)
    ruta = fields.Many2one("circulacion.ruta", string="Ruta*", required=True)

    # publicacion
    empresa_id = fields.Many2one("circulacion.empresa", string="Empresa")
    publicacion_id = fields.Many2one("circulacion.publicacion", string="Publicación")
    tipo_publicacion_id = fields.Many2one(
        "circulacion.tipopublicacion", string="Tipo de Publicación"
    )
    tipo_portada_id = fields.Many2one(
        "circulacion.tipoportada", string="Tipo de Portada"
    )
    asesor = fields.Many2one("circulacion.asesor")
    no_voceadores = fields.Integer(string="No. de Voceadores")
    anotaciones = fields.Text(string="Anotaciones")
    estado = fields.Char(
        compute="_compute_estado_cliente",
        store=True,
        string="Estado",
    )

    # @api.depends("cliente")
    # def _compute_cliente_id(self):
    #     for record in self:
    #         record.id_cliente = record.cliente.id if record.cliente else False

    @api.depends("cliente")
    def _compute_estado_cliente(self):
        for record in self:
            if record.cliente:
                record.estado = record.cliente.estado
            else:
                record.cliente_info = ""

    @api.depends("cliente")
    def _compute_cliente_info(self):
        for record in self:
            if record.cliente:
                record.cliente_info = "{} {} (ID: {})".format(
                    record.cliente.name, record.cliente.apellido, record.cliente.id
                )
            else:
                record.cliente_info = ""

    @api.onchange("country_id")
    def _onchange_country_id(self):
        self.state_id = False
        self.city_id = False
        return {"domain": {"state_id": [("country_id", "=", self.country_id.id)]}}

    @api.onchange("state_id")
    def _onchange_state_id(self):
        self.city_id = False
        return {"domain": {"city_id": [("state_id", "=", self.state_id.id)]}}

    @api.onchange("city_id")
    def _onchange_city_id(self):
        self.ruta = False
        return {"domain": {"ruta": [("city_id", "=", self.city_id.id)]}}

    # Funciones para actualizar el dominio dinámicamente
    @api.onchange("empresa_id")
    def _onchange_empresa_id(self):
        self.publicacion_id = False
        self.tipo_publicacion_id = False
        self.tipo_portada_id = False
        return {
            "domain": {
                "publicacion_id": [
                    (
                        "empresa_id",
                        "=",
                        self.empresa_id.id if self.empresa_id else False,
                    )
                ]
            }
        }

    @api.onchange("publicacion_id")
    def _onchange_publicacion_id(self):
        self.tipo_publicacion_id = False
        self.tipo_portada_id = False
        return {
            "domain": {
                "tipo_publicacion_id": [
                    (
                        "publicacion_id",
                        "=",
                        self.publicacion_id.id if self.publicacion_id else False,
                    )
                ]
            }
        }

    @api.onchange("tipo_publicacion_id")
    def _onchange_tipo_publicacion_id(self):
        self.tipo_portada_id = False
        return {
            "domain": {
                "tipo_portada_id": [
                    (
                        "publicacion_id",
                        "=",
                        self.publicacion_id.id if self.publicacion_id else False,
                    )
                ]
            }
        }


class asesor(models.Model):
    _name = "circulacion.asesor"
    _description = "circulacion.asesor"

    name = fields.Char(string="Nombre")


class supervisor(models.Model):
    _name = "circulacion.supervisor"
    _description = "circulacion.supervisor"

    name = fields.Char(string="Nombre")


class transportista(models.Model):
    _name = "circulacion.transportista"
    _description = "circulacion.transportista"

    name = fields.Char(string="Nombre")


class cobrador(models.Model):
    _name = "circulacion.cobrador"
    _description = "circulacion.cobrador"

    name = fields.Char(string="Nombre")
