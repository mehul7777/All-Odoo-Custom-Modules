from odoo import api, fields, models


class ProductTemplateInfo(models.Model):
    _inherit = 'product.template'

    can_be_rented = fields.Boolean(string="Can be Rented", default=False)
    rent_price = fields.Integer(string="Rent Price")
