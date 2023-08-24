# -*- coding: utf-8 -*-
# from odoo import http


# class Circulacion(http.Controller):
#     @http.route('/circulacion/circulacion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/circulacion/circulacion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('circulacion.listing', {
#             'root': '/circulacion/circulacion',
#             'objects': http.request.env['circulacion.circulacion'].search([]),
#         })

#     @http.route('/circulacion/circulacion/objects/<model("circulacion.circulacion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('circulacion.object', {
#             'object': obj
#         })
