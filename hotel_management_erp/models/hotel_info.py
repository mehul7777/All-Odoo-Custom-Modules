from odoo import api, fields, models, _


class HotelInfo(models.Model):
    _name = 'hotel.info'
    _rec_name = 'room_number'

    hotel_name = fields.Char("Hotel Name")
    room_number = fields.Integer("Room Number")
    floor_number = fields.Integer("Floor Number")

    # For smart button
    def action_open_sale_order_cust(self):
        return {
            'name': _("Sales Order"),
            'view_mode': 'form',
            'view_type': 'form',
            'view_id': False,
            'res_model': 'sale.order',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }


class PurchaseOrder2(models.Model):
    _inherit = "purchase.order"

    # This will create invoice by confirming purchase order
    def button_confirm(self):
        res = super(PurchaseOrder2, self).button_confirm()
        if self.state == "purchase":
            return self.action_create_invoice()

