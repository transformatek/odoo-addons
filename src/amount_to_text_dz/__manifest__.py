# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#
# Copyright (c) 2016  - Osis - www.osis-dz.net

# Copyright (c) 2021 TransformaTek.dz  (<https://transformatek.dz/>)


{
    'name': 'Algeria - Amount to Text',
    'version': '14.0',
    'category': 'Accounting',
    'website': 'https://transformatek.dz/',
    'summary': 'This is the module print amount to Text with fiscal timbre.',
    'license': 'AGPL-3',
    'description': """
This is the module print amount to Text with fiscal timbre.
========================================================================

This module applies to companies based in Algeria.

**Email:** contact@osis.dz
""",
    'author': 'Osis + TransformaTek',
    'website': 'https://transformatek.dz/',
    'version': '14.0.0.0.0',
    # 'depends': ['l10n_dz_timbre'],
    'data': [
        'views/order_invoice.xml',

    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
