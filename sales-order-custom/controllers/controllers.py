# -*- coding: utf-8 -*-
# from odoo import http


# class Sales-order-custom(http.Controller):
#     @http.route('/sales-order-custom/sales-order-custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales-order-custom/sales-order-custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales-order-custom.listing', {
#             'root': '/sales-order-custom/sales-order-custom',
#             'objects': http.request.env['sales-order-custom.sales-order-custom'].search([]),
#         })

#     @http.route('/sales-order-custom/sales-order-custom/objects/<model("sales-order-custom.sales-order-custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales-order-custom.object', {
#             'object': obj
#         })
