# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
import base64


class TPE(models.Model):
    _name = "tpe.tpe"
    _description = "Terminal de Paiement Électronique"

    serie_number = fields.Char(string="Numéro de série")
    name = fields.Char(string="Nom")
    bank_id = fields.Many2one("tpe.banque", string="Banque")
    operator = fields.Selection(
        [("mobilis", "Mobilis"), ("djezzy", "Djezzy"), ("ooredoo", "Ooredoo")],
        string="Opérateur",
    )
    constructor_id = fields.Many2one(
        "tpe.constructor",
        string="Constructeur",
        related="model_id.constructor_id",
        store=True,
    )
    contact_id = fields.Many2one("res.partner", string="Contact")
    model_id = fields.Many2one("tpe.model", string="Modèle")
    observation = fields.Text(string="Observation")

    # TODO Add field state [new, planned, in_progress, done, blocked, cancelled]

    # TODO Add field wilaya many2One
    
    # TODO Add field installation date 
    
    # TODO Add field order (commande) 

    def action_print_tpe_report(self):
        """Action pour générer le rapport PDF"""
        return self.env.ref(
            "tpe_managment.action_report_tpe_installation"
        ).report_action(self)
