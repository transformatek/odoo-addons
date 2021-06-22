# -*- coding: utf-8 -*-
{
    'name': "Maintenance Planning",

    'summary': """
        This module allow maintenace teams to plan their interventions with 
        predefined operations and materials""",

    'description': """
        This module allow maintenace teams to plan their interventions with 
        predefined operations and materials
    """,

    # Categories can be used to filter modules in modules listing
    'category': 'Maintenance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['maintenance', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'installable': True,
    'application': False,
}