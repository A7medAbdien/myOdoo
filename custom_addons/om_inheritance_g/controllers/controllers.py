# -*- coding: utf-8 -*-
# from odoo import http


# class OmInheritanceG(http.Controller):
#     @http.route('/om_inheritance_g/om_inheritance_g', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_inheritance_g/om_inheritance_g/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_inheritance_g.listing', {
#             'root': '/om_inheritance_g/om_inheritance_g',
#             'objects': http.request.env['om_inheritance_g.om_inheritance_g'].search([]),
#         })

#     @http.route('/om_inheritance_g/om_inheritance_g/objects/<model("om_inheritance_g.om_inheritance_g"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_inheritance_g.object', {
#             'object': obj
#         })
