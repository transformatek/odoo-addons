# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
import base64


class TPE(models.Model):
    _name = "tpe.tpe"
    _description = "Terminal de Paiement Électronique"

    serie_number = fields.Char(string="Numéro de série")
    name = fields.Char(string="Nom")
    bank_name = fields.Char(string="Banque")

    operator = fields.Selection(
        [("MOBILIS", "MOBILIS"), ("DJEZZY", "DJEZZY"), ("OOREDOO", "OOREDOO")],
        string="Opérateur",
    )
    constructor_name = fields.Char(string="Constructeur",default="ENIE")
    # contact_id = fields.Many2one("res.partner", string="Contact")
    company_id = fields.Many2one(
        "res.company",
        string="Société",
    )

    contact_name = fields.Char(string="Nom contact")
    enseigne = fields.Char(string="Enseigne")
    mobile = fields.Char(string="Mobile")
    street = fields.Char(string="Rue")
    city = fields.Char(string="Ville")

    model_name = fields.Char(string="Modèle")
    terminal_id = fields.Char(string="ID du terminal")
    observation = fields.Text(string="Observation")

    state = fields.Selection(
        [
            ("new", "Nouveau"),
            ("planned", "Planifié"),
            ("in_progress", "En cours"),
            ("done", "Terminé"),
            ("blocked", "Bloqué"),
            ("cancelled", "Annulé"),
        ],
        string="État",
        default="new",
        tracking=True,
    )

    wilaya_name = fields.Char(string="Wilaya")
    # wilaya_id = fields.Many2one("res.country.state", string="Wilaya")

    installation_date = fields.Date(string="Date d'installation")
    order = fields.Char(string="Commande")

    def action_print_tpe_report(self):
        """Action pour générer le rapport PDF"""
        return self.env.ref(
            "tpe_managment.action_report_tpe_installation"
        ).report_action(self)
