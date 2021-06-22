# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MaintenanceOperationMaterialLine(models.Model):
    _name = 'maintenance_planning.required_material'
    _description = 'Required material for maintenance'

    operation_id = fields.Many2one('maintenance_planning.operation', string='Operation',
                                ondelete='restrict', index=True)

    product_id = fields.Many2one(
        'product.product', 'Material',
        domain="[('type', 'in', ['product', 'consu'])]", 
        required=True)

    qty_required = fields.Integer('Quantity')
    comment = fields.Char('Comment') 


class MaintenanceOperation(models.Model):
    _name = 'maintenance_planning.operation'
    _description = 'Maintenance operation'

    name = fields.Char('Name', required=True)

    maintenance_duration = fields.Float(help="Maintenance Duration in hours.")

    periodicity = fields.Selection([('7', 'Week'), ('15', '2 Weeks'), ('30', 'Month'), 
                                    ('60', 'Two months'), ('90', 'Three months'), 
                                    ('180', 'Six months'),('365', 'Year')], 
                                    string='Periodicity', required=True)

    equipment_id = fields.Many2one('maintenance.equipment', string='Equipment',
                                   ondelete='restrict', index=True, required=True)

    required_material_ids = fields.One2many('maintenance_planning.required_material', 
                                            'operation_id', ondelete='cascade',
                                             help='Required material for maintenance operation')

    note = fields.Text('Note')


class MaintenancePlanning(models.Model):
    _inherit = 'maintenance.equipment'

    maintenance_operation_ids = fields.One2many('maintenance_planning.operation', 
                                        'equipment_id', help='Related maintenance operation')
    

# class MaintenancePlanning(models.Model):
#     _inherit = 'maintenance.request'

#     maintenance_operation_ids = fields.One2many('maintenance_planning.operation', 
#                                         'request_id', help='Related maintenance operation')
    
    
    # required_material_ids = fields.One2many('maintenance_planning.required_material', '')


# class my_module(models.Model):
#     _name = 'my_module.my_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

