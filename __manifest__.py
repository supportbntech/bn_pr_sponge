# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'SPONGE',
    'category': 'All',
    'summary': 'Sponge customizations',
    'author': 'Slomax@BnTechn',
    'description': """
        Sponge project customizations
    """,
    'depends': ['base', 'purchase', 'account', 'sale'],
    'data': [
        'reports/bn_inherit_layout.xml',
        'reports/bn_inherit_invoice.xml',
        'views/bn_inherit_company.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'OPL-1',
}

