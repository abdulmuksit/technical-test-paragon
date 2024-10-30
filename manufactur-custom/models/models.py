# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import UserError

class MrpBoM(models.Model):
    _inherit = 'mrp.bom'

    production_time = fields.Float(string="Estimated Production Time (hours)")

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    estimated_production_time = fields.Float(string="Estimated Production Time (hours)", readonly=True)
    is_plan = fields.Boolean(default=False)

    @api.onchange('bom_id')
    def _onchange_bom_id(self):
        if self.bom_id:
            self.estimated_production_time = self.bom_id.production_time or 0.0
        else:
            self.estimated_production_time = 0.0

    def action_plan_production(self):
        for production in self:
            if production.estimated_production_time > 0 and production.date_planned_start:
                date_finish = production.date_planned_start + timedelta(hours=production.estimated_production_time)
                production.write({
                    'date_start': production.date_planned_start,
                    'date_finished': date_finish,
                    'date_planned_finished': date_finish
                })
            elif production.estimated_production_time == 0:
                raise UserError('Field Estimated Production Time (hours) belum terisi, silahkan isi terlebih dahulu pada menu BoM')
            elif not production.date_planned_start:
                raise UserError('Field Scheduled Date belum terisi, silahkan isi terlebih dahulu')

            production.is_plan = True
