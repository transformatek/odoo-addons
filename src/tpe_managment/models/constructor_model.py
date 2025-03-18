# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Constructor(models.Model):
    _name = "tpe.constructor"
    _description = "Constructeur"

    name = fields.Char(string="Nom")
