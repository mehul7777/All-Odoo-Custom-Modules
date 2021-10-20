from odoo import api, fields, models


class CollegeInfo(models.Model):
    _name = 'college.info'
    _rec_name = ''

    college_name = fields.Char("College Name")
    college_address = fields.Text("College Address")
    principle_name = fields.Char("Principle Name")
    vice_principle_name = fields.Char("Vice Principle Name")
    total_no_of_staff = fields.Integer("Number of Staff")
    total_no_of_student = fields.Integer("Number of Student")
    contact_no = fields.Integer("Contact Number")
