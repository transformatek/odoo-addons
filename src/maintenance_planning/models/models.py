# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class MaintenanceOperation(models.Model):
    _name = 'maintenance_planning.operation'
    _description = 'Maintenance operation'

    name = fields.Char('Nom', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    maintenance_duration = fields.Float('Durée', help="Maintenance Duration in hours.")

    periodicity = fields.Selection([('7', 'Semaine'), ('15', '2 Semaines'), ('30', 'Mois'), 
                                    ('60', 'Deux mois'), ('90', 'Trois mois'), 
                                    ('180', 'Six mois'),('365', 'Un ans')], 
                                    string='Periodicité', required=True)

    equipment_id = fields.Many2one('maintenance.equipment', string='Equipment',
                                   ondelete='cascade', index=True, required=True)

    # required_material_ids = fields.One2many('maintenance_planning.required_material', 
    #                                         'operation_id', ondelete='cascade',
    #                                          help='Required material for maintenance operation')

    note = fields.Text('Note')


class MaintenancePlanningEquipement(models.Model):
    _inherit = 'maintenance.equipment'

    maintenance_operation_ids = fields.One2many('maintenance_planning.operation', 
                                        'equipment_id', ondelete='cascade',
                                        help='Related maintenance operation')
    

class MaintenanceRequestMaterialLine(models.Model):
    _name = 'maintenance_planning.required_material'
    _description = 'Required material for maintenance'

    
    sequence = fields.Integer(string='Sequence', default=10)
    request_id = fields.Many2one('maintenance.request', string='Requête',
                                ondelete='cascade', index=True)

    product_id = fields.Many2one('product.product', 'Matériel nécessaire',
                                domain="[('type', 'in', ['product', 'consu'])]", 
                                required=True)

    qty_required = fields.Integer('Quantité requise')
    comment = fields.Char('Commentaire') 

    qty_available_today = fields.Float('Quantité disponible', compute='_compute_qty_at_date')
    forecasted_issue = fields.Boolean(compute='_compute_qty_at_date')

    @api.depends('product_id', 'qty_required')
    def _compute_qty_at_date(self):
        for line in self:
            line.qty_available_today = line.product_id.qty_available - line.qty_required
            line.forecasted_issue = True if line.qty_available_today <= 0 else False

class MaintenancePlanningRequest(models.Model):
    _inherit = 'maintenance.request'

    maintenance_operation_id = fields.Many2one('maintenance_planning.operation', 'Operation',
                                        help='Related maintenance operation')
        
    required_material_ids = fields.One2many('maintenance_planning.required_material', 
                                            'request_id', ondelete='cascade',
                                            help='Required material for maintenance operation')



