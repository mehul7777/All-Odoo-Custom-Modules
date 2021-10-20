from odoo import api, fields, models


class HotelInfo(models.Model):
    _name = 'hotel.info'
    _rec_name = 'room_number'

    hotel_name = fields.Char("Hotel Name")
    room_number = fields.Integer("Room Number")
    floor_number = fields.Integer("Floor Number")


class PurchaseOrder2(models.Model):
    _inherit = "purchase.order"

    # This will create invoice by confirming purchase order
    def button_confirm(self):
        res = super(PurchaseOrder2, self).button_confirm()
        if self.state == "purchase":
            return self.action_create_invoice()

