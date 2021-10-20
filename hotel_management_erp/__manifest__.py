# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hotel Management ERP',
    'version': '1.0',
    'author': 'Mehul Darji',
    'category': 'Tutorials',
    'summary': 'Tutorials of Hotel Management ERP',
    'description': "We are learning what is odoo and development in odoo",
    'website': 'https://www.odoo.com',
    'depends': [
        'base', 'sale', 'purchase'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hotel_info_views.xml',
        'views/other_expense_views.xml',
        'views/sale_order_inherit.xml',


    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
