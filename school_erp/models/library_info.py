from odoo import api, fields, models


class LibraryInfo(models.Model):
    _name = 'library.info'

    book_name = fields.Char("Name", required=True)
    book_author = fields.Char("Book Author")
    book_id = fields.Integer("Book ID", required=True)
    book_type = fields.Char("Book Type")

    library_ids = fields.One2many(comodel_name='student.info', inverse_name='student1_id', string='Students')

    # issue_date = fields.Datetime("Issue Date")
    # return_date = fields.Datetime("Return Date")

    # override use create and write
    def write(self, vals):
        print('Vals', vals)
        if vals:
            vals.update({'book_type': 'Fun'})
        return super(LibraryInfo, self).write(vals)

    @api.model
    def create(self, vals):
        print('CREATE CALL', vals)
        print('Create working')
        vals['book_type'] = 'Mystery'
        return super(LibraryInfo, self).create(vals)
