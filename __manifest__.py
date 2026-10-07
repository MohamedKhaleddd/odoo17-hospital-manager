# -*- coding: utf-8 -*-
{
    'name': "Hospital Manager",

    'summary': "My Hospital App",

    'description': """
        Good view of patients. doctors and get best reports
    """,

    'author': "Hospital",
    'website': "https://www.hospital.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','mail'],

    'data': [
        'security/ir.model.access.csv',
        'security/rule.xml',
        'wizards/add_appointment.xml',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml',
        'views/doctor.xml',
        'views/appointment.xml',
        'views/medicines.xml',
        'views/menus.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}