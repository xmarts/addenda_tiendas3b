# -*- coding: utf-8 -*-
from odoo import http

# class AddendaTiendas3b(http.Controller):
#     @http.route('/addenda_tiendas3b/addenda_tiendas3b/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addenda_tiendas3b/addenda_tiendas3b/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addenda_tiendas3b.listing', {
#             'root': '/addenda_tiendas3b/addenda_tiendas3b',
#             'objects': http.request.env['addenda_tiendas3b.addenda_tiendas3b'].search([]),
#         })

#     @http.route('/addenda_tiendas3b/addenda_tiendas3b/objects/<model("addenda_tiendas3b.addenda_tiendas3b"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addenda_tiendas3b.object', {
#             'object': obj
#         })