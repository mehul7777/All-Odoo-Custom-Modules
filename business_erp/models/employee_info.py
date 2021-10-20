from odoo import api, fields, models


class EmployeeInfo(models.Model):
    _name = 'employee.info'

    name = fields.Char('Name',required=True)
    middle_name = fields.Char('Middle Name')
    employee_age = fields.Integer('Age')
    employee_field = fields.Selection([('PY', 'Python Developer'),
                                    ('JS', 'JavaScript Developer'),
                                    ('HTML', 'Web Developer'),
                                    ('JAVA', 'Java Developer'),],
                                      'Fields', required=True)
    employee_salary = fields.Float("Salary")
    city = fields.Char('City', default ='Mumbai', readonly =True)
    gender_male = fields.Selection([('male', 'Male'),
                                    ('female', 'Female')],
                                      'Gender', required=True)
    is_pwd = fields.Boolean('Is Phycially Handiacpped?')


