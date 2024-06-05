# -*- coding: utf-8 -*-
# from odoo import http


# class ZinfogSales(http.Controller):
#     @http.route('/zinfog_sales/zinfog_sales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zinfog_sales/zinfog_sales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zinfog_sales.listing', {
#             'root': '/zinfog_sales/zinfog_sales',
#             'objects': http.request.env['zinfog_sales.zinfog_sales'].search([]),
#         })

#     @http.route('/zinfog_sales/zinfog_sales/objects/<model("zinfog_sales.zinfog_sales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zinfog_sales.object', {
#             'object': obj
#         })
