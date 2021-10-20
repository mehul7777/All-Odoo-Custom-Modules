from odoo import api, fields, models


class CulturalFest(models.Model):
    _name = 'cultural.fest'
    _rec_name = 'fest_name'

    fest_name = fields.Char('Festival Name')
    standard_id = fields.Many2one('standard.info', 'Standard Name')
    number_of_participants = fields.Integer('Number of Participants')
    festival_information = fields.Text('Fest Information')

    student_fees_ids = fields.One2many(comodel_name="cultural.fest.line", inverse_name="name_id")

    @api.model
    def default_get(self, fields):
        res = super(CulturalFest, self).default_get(fields)
        res['fest_name'] = 'Dance'
        res['standard_id'] = 2
        res['number_of_participants'] = 20
        res['festival_information'] = 'Every group must have 50% boys and 50% girls'
        return res


class CulturalFestLine(models.Model):
    _name = 'cultural.fest.line'
    _rec_name = 'stud_name'

    stud_name = fields.Many2one(comodel_name="student.info", string="Student Name")
    name_id = fields.Many2one(comodel_name="cultural.fest")
    competition = fields.Char(related="name_id.fest_name", string="Competition")
    fees = fields.Float(string="Fees")
    fees_calculator = fields.Boolean(string="Fees Calculator")
    budget_reset_ids = fields.One2many(comodel_name="student.info", inverse_name="cultural_fest_line_id")  # no use

    def unlink(self):
        print("Unlink is running")
        for record in self:
            print(record)
            for rec in record.stud_name:
                print(rec.budget)
                budget_remained = rec.budget + record.fees
                rec.budget = budget_remained
        return super(CulturalFestLine, self).unlink()

    @api.onchange('fees')
    def onchange_fees_id(self):
        if self.fees:
            print(self.fees)
            self.stud_name.budget -= self.fees
            self.fees_calculator = True