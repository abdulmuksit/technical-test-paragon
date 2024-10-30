# -*- coding: utf-8 -*-
# from odoo import http


# class Sync-master-data(http.Controller):
#     @http.route('/sync-master-data/sync-master-data', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sync-master-data/sync-master-data/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sync-master-data.listing', {
#             'root': '/sync-master-data/sync-master-data',
#             'objects': http.request.env['sync-master-data.sync-master-data'].search([]),
#         })

#     @http.route('/sync-master-data/sync-master-data/objects/<model("sync-master-data.sync-master-data"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sync-master-data.object', {
#             'object': obj
#         })
