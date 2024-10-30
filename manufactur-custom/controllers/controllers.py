# -*- coding: utf-8 -*-
# from odoo import http


# class Manufactur-custom(http.Controller):
#     @http.route('/manufactur-custom/manufactur-custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manufactur-custom/manufactur-custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('manufactur-custom.listing', {
#             'root': '/manufactur-custom/manufactur-custom',
#             'objects': http.request.env['manufactur-custom.manufactur-custom'].search([]),
#         })

#     @http.route('/manufactur-custom/manufactur-custom/objects/<model("manufactur-custom.manufactur-custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manufactur-custom.object', {
#             'object': obj
#         })
