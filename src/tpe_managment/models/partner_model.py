# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Contact(models.Model):
    _inherit = "res.partner"

    trade_sign = fields.Char(string="Enseigne du commerce")
