# -*- coding: utf-8 -*-
# from odoo import http


# class OmHospitalG(http.Controller):
#     @http.route('/om_hospital_g/om_hospital_g', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_hospital_g/om_hospital_g/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_hospital_g.listing', {
#             'root': '/om_hospital_g/om_hospital_g',
#             'objects': http.request.env['om_hospital_g.om_hospital_g'].search([]),
#         })

#     @http.route('/om_hospital_g/om_hospital_g/objects/<model("om_hospital_g.om_hospital_g"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_hospital_g.object', {
#             'object': obj
#         })
