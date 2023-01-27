from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one(
    string='Confirmed User',
    comodel_name='res.users',
    )