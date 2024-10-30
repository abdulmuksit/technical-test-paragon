# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cancelReason(models.Model):
    _name = 'cancel.reason'

    name = fields.Char("Name")
    description = fields.Text("Description")
    active = fields.Boolean("Active", default=True)

class CancelReasonWizard(models.TransientModel):
    _name = 'cancel.reason.wizard'
    _description = 'Cancel Reason Wizard'

    cancel_reason_id = fields.Many2one('cancel.reason', string="Cancel Reason", required=True)
    order_id = fields.Many2one('sale.order', string="Sales Order", required=True)

    def action_confirm(self):
        self.order_id.cancel_reason_id = self.cancel_reason_id.id
        self.order_id.with_context(disable_cancel_warning=True).action_cancel()
        return {'type': 'ir.actions.act_window_close'}

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    cancel_reason_id = fields.Many2one('cancel.reason', string="Cancel Reason", readonly=True)

    def action_cancel(self):
        print("Masuk")
        for order in self:
            print("Masuk pak")
            if not order.cancel_reason_id:
                return {
                    'type': 'ir.actions.act_window',
                    'name': 'Select Cancel Reason',
                    'view_mode': 'form',
                    'res_model': 'cancel.reason.wizard',
                    'target': 'new',
                    'context': {'default_order_id': order.id},
                }
        return super(SaleOrder, self).action_cancel()
