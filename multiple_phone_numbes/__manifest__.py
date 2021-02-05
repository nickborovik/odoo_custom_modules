# -*- coding: utf-8 -*-
{
    'name': 'Multiple Phone Numbers',
    'summary': 'This module adds new model Phones to odoo',
    'author': 'Nikita Borovik',
    'support': 'nick.borovik@gmail.com',
    'license': 'AGPL-3',
    'category': 'Hidden',
    'version': '1.0',
    'description': """
Multiple Phone Numbers
======================
Create multiple phone numbers for your contacts or partners
    """,
    'depends': [
        'base',
        'contacts'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/phones_views.xml'
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
    'post_init_hook': '_copy_mobile_and_phone_numbers',
}
