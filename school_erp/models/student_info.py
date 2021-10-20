from odoo import api, fields, models


class StudentInfo(models.Model):
    _name = 'student.info'

    name = fields.Char('Name', required=True)
    middle_name = fields.Char('Middle Name')
    student_age = fields.Integer('Age')
    city = fields.Char('City', default='Mumbai', readonly=True)
    gender_male = fields.Selection([('male', 'Male'),
                                    ('female', 'Female')],
                                   'Gender')

    # gender_id = fields.Many2one(comodel_name='male.info')
    # gender_id1 = fields.Many2one(comodel_name='female.info')

    is_pwd = fields.Boolean('Is Phycially Handiacpped?')
    standard_id = fields.Many2one('standard.info', 'Standard')
    division = fields.Selection([('div_a', 'A'),
                                 ('div_b', 'B'),
                                 ('div_c', 'C'),
                                 ('std_d', 'D'), ],
                                'Division', required=True, related='standard_id.division')
    teacher_name = fields.Char(related='standard_id.teacher_name')
    student_id = fields.Many2one(comodel_name='standard.info', string='Student Id', )
    sports_id = fields.Many2one(comodel_name='sports.activity', string='Game')

    student1_id = fields.Many2one(comodel_name='library.info')
    issue_date = fields.Datetime("Issue Date")
    return_date = fields.Datetime("Return Date")
    fest_ids = fields.Many2many(comodel_name='cultural.fest', relation='student_info_cultural_fest_rel',
                                column1='stud_id', column2='fest_id', string='Groups')
    scholar_ship_ids = fields.Many2many(comodel_name='scholarship.info', relation='student_info_scholarship_info_rel',
                                        column1='stud_id', column2='scholarship_id', string='Scholarship(s)')
    teachers_ids = fields.One2many(comodel_name='teachers.subjects.line', inverse_name='teacher1_id')

    educational_quota = fields.Selection([('class_1', '10%'),
                                          ('class_2', '15%'),
                                          ('class_3', '20%'),
                                          ('class_4', '30%')],
                                          'Educational Qouta')
    budget = fields.Float(string="Budget")
    cultural_fest_line_id = fields.Many2one(comodel_name="cultural.fest.line")  # no use
    cultural_fest_line_ids = fields.One2many(comodel_name="cultural.fest.line", inverse_name="stud_name")

    def change_age(self):
        self.student_age = 25

    @api.onchange('is_pwd')
    def change_gender_on_cond(self):
        if self.is_pwd == True:
            self.educational_quota = 'class_3'
        else:
            self.educational_quota = 'class_1'

    is_reading = fields.Boolean(string="Reading")
    is_swimming = fields.Boolean(string="Swimming")
    is_dancing = fields.Boolean(string="Dancing")

    chemistry = fields.Integer(string="Chemistry")
    physics = fields.Integer(string="Physics")
    maths = fields.Integer(string="Maths")
    english = fields.Integer(string="English")
    total = fields.Integer(string="Total", compute='_compute_total_marks')
    percentage = fields.Float(string="Percentage", compute='_compute_percentage')
    status = fields.Char(string="Status", readonly=True)

    @api.depends("chemistry", "physics", "maths", "english")
    def _compute_total_marks(self):
        self.total = self.chemistry + self.physics + self.maths + self.english

    @api.depends("total", "status")
    def _compute_percentage(self):
        self.percentage = self.total * 100 / 400
        if self.percentage < 40:
            self.status = "Fail"
        else:
            self.status = "Pass"

    student_timetable = fields.Html(string="Student TimeTable")
    document = fields.Binary('Documents')


class TeachersSubjects(models.Model):
    _name = 'teachers.subjects.line'

    teacher1_id = fields.Many2one(comodel_name='student.info')

    subject_id = fields.Many2one(comodel_name='subject.info',string="Subjects")

    teacher_name_id = fields.Many2one(comodel_name='teacher.info')

    gender_id = fields.Many2one(comodel_name='student.info')  #This is of no use