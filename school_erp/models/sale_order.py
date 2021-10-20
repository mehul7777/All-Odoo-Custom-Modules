from odoo import api, fields, models


class SaleOrderInfor(models.Model):
    _inherit = 'sale.order'

    order_day_info = fields.Char('Order Day')
    sales_person_contact = fields.Integer('Contact Number')
    product_rank = fields.Integer('Product Rank (1-5)')  # This field is of no use
    product_quantity = fields.Float('Product Quantity')

    customer_email = fields.Char(related='partner_id.email', string="Customer Email")


class SaleOrderInfoRecord(models.Model):
    _inherit = 'sale.order.line'

    product_rank = fields.Integer('Product Rank (1-5)')
    product_quantity = fields.Float('Product Quantity')  # This field is of no use

    product_category = fields.Char('Product Category', readonly=True, related='product_id.product_tmpl_id.categ_id.name')
