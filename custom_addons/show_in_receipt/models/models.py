# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class show_in_receipt(models.Model):
#     _name = 'show_in_receipt.show_in_receipt'
#     _description = 'show_in_receipt.show_in_receipt'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
