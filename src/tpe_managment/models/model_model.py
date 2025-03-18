# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Model(models.Model):
    _name = "tpe.model"
    _description = "Modèle"

    name = fields.Char(string="Nom", required=True)
    constructor_id = fields.Many2one("tpe.constructor", string="Constructeur")
