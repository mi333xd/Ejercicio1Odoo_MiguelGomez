# -*- coding: utf-8 -*-
# from odoo import http


# class Tarea04-instituto(http.Controller):
#     @http.route('/tarea04-instituto/tarea04-instituto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tarea04-instituto/tarea04-instituto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tarea04-instituto.listing', {
#             'root': '/tarea04-instituto/tarea04-instituto',
#             'objects': http.request.env['tarea04-instituto.tarea04-instituto'].search([]),
#         })

#     @http.route('/tarea04-instituto/tarea04-instituto/objects/<model("tarea04-instituto.tarea04-instituto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tarea04-instituto.object', {
#             'object': obj
#         })

