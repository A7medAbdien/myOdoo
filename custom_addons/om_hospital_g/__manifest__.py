# -*- coding: utf-8 -*-
{
    'name': "om_hospitalG",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tagg_data.xml',
        'data/patient.tagg.csv',
        'views/views.xml',
        'wizard/cancel_appointment_wizard.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_view.xml',
        'views/appointment_view.xml',
        'views/templates.xml',
        'views/patient_tag_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'sequence': -100,
}
