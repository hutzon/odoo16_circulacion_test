# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cliente(models.Model):
    _name = "circulacion.cliente"
    _description = "circulacion.cliente"

    name = fields.Char(string="Nombre", required=True)
    fotografia = fields.Binary(string="Fotografía")
    apellido = fields.Char(string="Apellido(s)")
    empresa = fields.Char(string="Nombre de Compañia")
    nit = fields.Char(string="NIT")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    no_documento = fields.Char()
    talla = fields.Char()
    nombre_facturacion = fields.Char(string="Nombre de Facturación")
    dir_facturacion = fields.Char(string="Dirección de Facturación")
    telefono = fields.Char(string="Teléfonos")
    correo = fields.Char(string="Correo Electrónico")
    precio_unidad = fields.Float(
        default=1.66, readonly=True, digits=(16, 2), string="Precio por Unidad"
    )
    dias_validos_devolucion = fields.Integer(
        default=1, string="Días Válidos para Devolución"
    )
    cantidad_pedido = fields.Integer(default=0, string="Cantidad de Pedido Ordinario")
    cantidad_flete = fields.Integer(default=0, string="Cantidad de Flete")
    cantidad_promocion = fields.Integer(default=0, string="Cantidad de Promoción")
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
        string="Canales de Facturación",
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
        required=True,
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
        string="Canales de Facturación",
        default="sectores_metropolitanos",
        required=True,
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
        string="Canales de Distribución",
        default="sectores_metropolitanos",
        required=True,
    )

    estado = fields.Selection(
        [
            ("activo", "Activo"),
            ("inactivo", "Inactivo"),
        ],
        string="Estado",
        default="activo",
        required=True,
    )

    facturar_pedidos = fields.Selection(
        [
            ("si", "Si"),
            ("no", "No"),
        ],
        string="Facturar Pedidos",
        default="si",
        required=True,
    )


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

    name = fields.Char(string="Nombre del Sector", required=True)
    calle_avenida = fields.Char(string="Calle o Avenida")
    no_casa = fields.Char(string="No. de Casa")
    no_apartamento = fields.Char(string="No. de Apartamento")
    zona = fields.Char(string="Zona")
    colonia_barrio_aldea = fields.Char(string="Colonia, Barrio o Aldea")
    cliente = fields.Many2one("circulacion.cliente")
    cliente_info = fields.Char(
        string="Información del Cliente", compute="_compute_cliente_info"
    )

    orden_ruta = fields.Integer(default=1, string="Orden de la Ruta")
    tipo_direccion = fields.Selection(
        [
            ("entrega", "Entrega"),
            ("facturacion", "Facturación"),
            ("ambas", "Ambas"),
        ],
        string="Tipo de Direccion",
        default="ambas",
        required=True,
    )

    # Campos para Paises
    country_id = fields.Many2one("circulacion.country", string="Pais")
    state_id = fields.Many2one("circulacion.state", string="Departamento")
    city_id = fields.Many2one("circulacion.city", string="Municipio")
    ruta = fields.Many2one("circulacion.ruta", string="Ruta")

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

    @api.depends("cliente")
    def _compute_cliente_info(self):
        for record in self:
            if record.cliente:
                record.cliente_info = "{} {} (ID: {})".format(
                    record.cliente.name, record.cliente.apellido, record.cliente.id
                )

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
