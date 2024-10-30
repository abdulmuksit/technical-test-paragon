# -*- coding: utf-8 -*-

from odoo import models, fields, api


class stockQuant(models.Model):
    _inherit = 'stock.quant'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_approval', 'Waiting for Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('done', 'Done'),
    ], string="Status", default='waiting_approval', readonly=True, tracking=True)

    def button_approved(self):
        if self.state == 'waiting_approval':
            self.state = 'approved'

    def button_rejected(self):
        if self.state == 'waiting_approval':
            self.state = 'rejected'
            self.action_set_inventory_quantity_to_zero()
            self.state = 'draft'

    def action_apply_inventory(self):
        res = super(stockQuant, self).action_apply_inventory()
        self.state = 'done'
        return res
    
    @api.onchange('inventory_quantity_set')
    def _onchange_inventory_quantity_set(self):
        if self.inventory_quantity_set:
            self.state = 'waiting_approval'


