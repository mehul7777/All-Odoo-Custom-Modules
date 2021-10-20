# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Business ERP',
    'version': '1.0',
    'author': 'Mehul Darji',
    'category': 'Tutorials',
    'summary': 'Tutorials of Business ERP',
    'description': "We are learning what is odoo and development in odoo",
    'website': 'https://www.odoo.com',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_info_views.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
