
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ProjectDelete(models.TransientModel):
    _name = 'maintenance_planning.plan.requests.wizard'
    _description = 'Plan maintenance requests'

    # project_ids = fields.Many2many('project.project', string='Projects')
    # task_count = fields.Integer(compute='_compute_task_count')
    # projects_archived = fields.Boolean(compute='_compute_projects_archived')

    def confirm_plan(self):
       
        return self.env.ref("maintenance.hr_equipment_request_action_cal").read()[0]