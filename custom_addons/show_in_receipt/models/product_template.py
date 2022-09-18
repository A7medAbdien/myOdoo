from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    showInReceipt = fields.Boolean(
        string='showInReceipt',
    )
