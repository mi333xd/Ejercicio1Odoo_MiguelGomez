# -*- coding: utf-8 -*-
# from odoo import http


# class Tarea03-hospital(http.Controller):
#     @http.route('/tarea03-hospital/tarea03-hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tarea03-hospital/tarea03-hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tarea03-hospital.listing', {
#             'root': '/tarea03-hospital/tarea03-hospital',
#             'objects': http.request.env['tarea03-hospital.tarea03-hospital'].search([]),
#         })

#     @http.route('/tarea03-hospital/tarea03-hospital/objects/<model("tarea03-hospital.tarea03-hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tarea03-hospital.object', {
#             'object': obj
#         })

