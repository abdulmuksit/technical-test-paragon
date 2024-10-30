# -*- coding: utf-8 -*-
# from odoo import http


# class Inventory-adjustment-custom(http.Controller):
#     @http.route('/inventory-adjustment-custom/inventory-adjustment-custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventory-adjustment-custom/inventory-adjustment-custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventory-adjustment-custom.listing', {
#             'root': '/inventory-adjustment-custom/inventory-adjustment-custom',
#             'objects': http.request.env['inventory-adjustment-custom.inventory-adjustment-custom'].search([]),
#         })

#     @http.route('/inventory-adjustment-custom/inventory-adjustment-custom/objects/<model("inventory-adjustment-custom.inventory-adjustment-custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventory-adjustment-custom.object', {
#             'object': obj
#         })
