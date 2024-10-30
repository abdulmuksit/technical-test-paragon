# -*- coding: utf-8 -*-
# from odoo import http


# class Inventory-custom(http.Controller):
#     @http.route('/inventory-custom/inventory-custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventory-custom/inventory-custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventory-custom.listing', {
#             'root': '/inventory-custom/inventory-custom',
#             'objects': http.request.env['inventory-custom.inventory-custom'].search([]),
#         })

#     @http.route('/inventory-custom/inventory-custom/objects/<model("inventory-custom.inventory-custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventory-custom.object', {
#             'object': obj
#         })
