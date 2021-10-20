from odoo import api, fields, models


class ScholarShipInfo(models.Model):
    _name = 'scholarship.info'
    _rec_name = 'scholar_ship_name'

    name_id = fields.Many2one('student.info', 'Student Name')
    scholar_ship_name = fields.Char('ScholarShip Name')

