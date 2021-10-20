from odoo import api, fields, models, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    product_ids = fields.One2many(comodel_name="products.detail", inverse_name="product_res_id")


class ProductsDetail(models.Model):
    _name = "products.detail"

    product_res_id = fields.Many2one(comodel_name="res.partner")
    res_id = fields.Many2one(comodel_name="product.product", string="Product")
    quantity = fields.Float("Quantity")
    price = fields.Float("Unit Price")
    res_uom = fields.Many2one("uom.uom")


class SaleOrder(models.Model):
    _inherit = "sale.order"

    verification_done = fields.Boolean("Verification Done")
    room_number_id = fields.Many2one("hotel.info")
    check_in_time = fields.Datetime(string="Check In Time") # No use

    # This will not allow to select same room number twice
    global used_room_no
    used_room_no = []
    @api.onchange("room_number_id")
    def RoomNoValidation(self):
        print("RoomNoValidation Running")
        for record in self.room_number_id:
            print(record.room_number)
            if record.room_number in used_room_no:
                raise ValidationError("Select other room number")
            else:
                used_room_no.append(record.room_number)
        print(used_room_no)

    @api.onchange("partner_id")
    def update_detail(self):
        for rec in self:
            print("rec", rec)
            lines = []
            for line in self.partner_id.product_ids:
                print("line", line)
                val = {
                    'product_id': line.res_id.id,
                    'product_uom_qty': line.quantity,
                    'product_uom': line.res_uom,
                    'price_unit': line.price,
                }
                lines.append((0, 0, val))
            rec.order_line = lines
            print("rec.order_line", rec.order_line)
            print("lines", lines)

    # This will create invoice by confirming sale order
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        if self.state == "sale":
            return {
                'name': _("Create Invoices"),
                'view_mode': 'form',
                'view_type': 'form',
                'view_id': False,
                'res_model': 'sale.advance.payment.inv',
                # 'res_id': self.action_view_sale_advance_payment_inv,
                'type': 'ir.actions.act_window',
                'target':'new'
            }


class SaleOrderRes(models.Model):
    _inherit = "sale.order.line"

    check_in_time = fields.Datetime(string="Check In Time")
    check_out_time = fields.Datetime(string="Check Out Time")
    number_of_hours = fields.Integer(string="Number of Hours", compute="difference_date", store=1)
    Number_of_person = fields.Integer(string="Number of Person")

    @api.depends('check_in_time', 'check_out_time')
    def difference_date(self):
        fmt = '%Y-%m-%d %H:%M:%S'
        if self.check_in_time and self.check_out_time:
            start_date = self.check_in_time
            end_date = self.check_out_time
            # print(start_date, type(start_date))
            # print(end_date, type(end_date))
            d1 = datetime.strptime(str(start_date), fmt)
            d2 = datetime.strptime(str(end_date), fmt)
            # diff = str(d2 - d1)
            # print(diff)
            # print(diff[:2])
            # self.number_of_hours = int(diff[:2])
            # if "day" or "days" in diff:
            #     if "days" in diff:
            #         self.number_of_hours = int(diff[0]) * 24
            #         self.price_unit = 1000 * int(diff[0])
            #     elif "1 day, 00" in diff:
            #         self.number_of_hours = 24
            #         self.price_unit = 1000 * int(diff[0])
            #     elif "1 day, 1" or "1 day, 2" in diff:
            #         self.number_of_hours = 48
            #         self.price_unit = 1000 * int(diff[0])
            diff = d2 - d1
            if self.check_out_time > self.check_in_time:
                days, seconds = diff.days, diff.seconds
                hours = days * 24 + seconds // 3600
                self.number_of_hours = hours
                if hours > 0 and hours <= 24:
                    self.product_uom_qty = 1
                else:
                    self.product_uom_qty = diff.days
            else:
                raise ValidationError("Invalid Time")