# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class om_hospital_g(models.Model):
#     _name = 'om_hospital_g.om_hospital_g'
#     _description = 'om_hospital_g.om_hospital_g'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
