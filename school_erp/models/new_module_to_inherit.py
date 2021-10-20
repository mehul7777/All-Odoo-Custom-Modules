from odoo import fields, models


class TeacherDetail(models.Model):
    _inherit = 'teacher.info'

    gender = fields.Selection([('male', 'Male'),
                                    ('female', 'Female')],
                                   'Gender')

