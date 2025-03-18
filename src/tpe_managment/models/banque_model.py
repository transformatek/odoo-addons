# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Banque(models.Model):
    _name = "tpe.banque"
    _description = "Banque"

    name = fields.Char(string="Nom")
    code = fields.Char(string="Code")
