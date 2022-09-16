# -*- coding: utf-8 -*-
# from odoo import http


# class ShowInRecepit(http.Controller):
#     @http.route('/show_in_recepit/show_in_recepit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/show_in_recepit/show_in_recepit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('show_in_recepit.listing', {
#             'root': '/show_in_recepit/show_in_recepit',
#             'objects': http.request.env['show_in_recepit.show_in_recepit'].search([]),
#         })

#     @http.route('/show_in_recepit/show_in_recepit/objects/<model("show_in_recepit.show_in_recepit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('show_in_recepit.object', {
#             'object': obj
#         })
