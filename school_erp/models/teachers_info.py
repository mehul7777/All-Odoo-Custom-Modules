from odoo import api, fields, models


class TeacherInfo(models.Model):
    _name = 'teacher.info'
    _rec_name = 'teacher_name'

    teacher_name = fields.Char("Teacher")
    teacher_ids = fields.Many2many(comodel_name='teacher.info', relation='teacher_info_student_info_rel',
                                   column1='teach_id', column2='stud_id', string='Teachers')  # This field is of no use
    class_teacher = fields.Char("Class")
    division = fields.Selection([('div_a', 'A'),
                                 ('div_b', 'B'),
                                 ('div_c', 'C'),
                                 ('std_d', 'D'), ],
                                'Division', required=True)
    subject = fields.Many2one(comodel_name='subject.info')
    teacher_id = fields.Many2one('teacher.info', 'Teacher')


class SubjectInfo(models.Model):
    _name = 'subject.info'
    _rec_name = 'subject_name'

    subject_name = fields.Char("Subject Name")
