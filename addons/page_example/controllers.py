# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)


class MiPrimerPagina(http.Controller):

    @http.route('/mi-primera-pagina', auth='public',website=True)
    def index(self, **kwargs):
        products = request.env["product.template"].search([])
        return request.render('page_example.mi_primera_pagina',{"products":products})