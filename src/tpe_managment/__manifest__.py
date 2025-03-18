# -*- coding: utf-8 -*-

{
    "name": "tpe_management",
    "ressource": """
        TPE MANAGEMENT
    """,
    "description": "TPE MANAGEMENT",
    "author": "My Company",
    "website": "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
    ],
    # always loaded
    "data": [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/banque_views.xml',
        'views/constructor_views.xml',
        'views/model_views.xml',
        'views/partner_views.xml',
        'views/tpe_views.xml',
        'report/installation_report.xml'
        
    ],
    "assets": {
    "web.assets_backend": [
        "tpe_managment/static/src/img/ssb.png",
    ],
    "web.assets_frontend": [
        "tpe_managment/static/src/img/ssb.png",
    ],
},


    "license": "Other proprietary",
    "application": True,
    "installable": True,
    "auto_install": False,
}
