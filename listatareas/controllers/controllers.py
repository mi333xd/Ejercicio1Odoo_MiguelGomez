# -*- coding: utf-8 -*-
# from odoo import http


# class Listatareas(http.Controller):
#     @http.route('/listatareas/listatareas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/listatareas/listatareas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('listatareas.listing', {
#             'root': '/listatareas/listatareas',
#             'objects': http.request.env['listatareas.listatareas'].search([]),
#         })

#     @http.route('/listatareas/listatareas/objects/<model("listatareas.listatareas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('listatareas.object', {
#             'object': obj
#         })

