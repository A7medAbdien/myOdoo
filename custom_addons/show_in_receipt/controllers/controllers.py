# -*- coding: utf-8 -*-
# from odoo import http


# class ShowInReceipt(http.Controller):
#     @http.route('/show_in_receipt/show_in_receipt', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/show_in_receipt/show_in_receipt/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('show_in_receipt.listing', {
#             'root': '/show_in_receipt/show_in_receipt',
#             'objects': http.request.env['show_in_receipt.show_in_receipt'].search([]),
#         })

#     @http.route('/show_in_receipt/show_in_receipt/objects/<model("show_in_receipt.show_in_receipt"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('show_in_receipt.object', {
#             'object': obj
#         })
