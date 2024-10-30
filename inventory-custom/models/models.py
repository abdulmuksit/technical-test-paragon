# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class stockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self, vals):
        res = super(stockPicking, self).create(vals)
        if res and res.location_dest_id:
            location_product_rule = self.env['location.product.rule'].search([('location_id','=',res.location_dest_id.id)])
            if location_product_rule:
                for move in res.move_ids_without_package:
                    if move.product_id.id not in location_product_rule.product_ids.ids:
                        raise UserError('Product %s tidak valid untuk lokasi %s' % (move.product_id.name, res.location_dest_id.name))
                    
                    for lot in move.lot_ids:
                        lot = lot.search([('name','=',lot.name)])
                        if lot.id not in location_product_rule.lot_ids.ids:
                            raise UserError('Lot %s tidak valid untuk lokasi %s' % (lot.name, res.location_dest_id.name))
        return res
    
    def write(self, vals):
        res = super(stockPicking, self).write(vals)
        if res and self.location_dest_id:
            location_product_rule = self.env['location.product.rule'].search([('location_id','=',self.location_dest_id.id)])
            if location_product_rule:
                for move in self.move_ids_without_package:
                    if move.product_id.id not in location_product_rule.product_ids.ids:
                        raise UserError('Product %s tidak valid untuk lokasi %s' % (move.product_id.name, self.location_dest_id.name))
                    
                    for lot in move.lot_ids:
                        lot = lot.search([('name','=',lot.name)])
                        if lot.id not in location_product_rule.lot_ids.ids:
                            raise UserError('Lot %s tidak valid untuk lokasi %s' % (lot.name, self.location_dest_id.name))
        return res

class stockMove(models.Model):
    _inherit = 'stock.move'

    @api.onchange('product_id', 'lot_ids')
    def _onchange_product_id_lot_ids(self):
        if self.product_id and self.picking_id and not self.picking_id.location_dest_id:
            raise UserError('Field source location belum terisi')

        if self.product_id and self.picking_id and self.picking_id.location_dest_id:
            location_product_rule = self.env['location.product.rule'].search([('location_id','=',self.picking_id.location_dest_id.id)])
            if location_product_rule:
                if self.product_id.id not in location_product_rule.product_ids.ids:
                    raise UserError('Product %s tidak valid untuk lokasi %s' % (self.product_id.name, self.picking_id.location_dest_id.name))

                for lot in self.lot_ids:
                    lot = lot.search([('name','=',lot.name)])
                    if lot.id not in location_product_rule.lot_ids.ids:
                        raise UserError('Lot %s tidak valid untuk lokasi %s' % (lot.name, self.picking_id.location_dest_id.name))

class LocationProductRule(models.Model):
    _name = 'location.product.rule'
    _description = 'Location Product Rules'

    location_id = fields.Many2one('stock.location', string="Location", required=True)
    lot_ids = fields.Many2many('stock.lot', string="Lot/Serial", required=True)
    product_ids = fields.Many2many('product.product', string="Product", readonly=True)

    @api.onchange('location_id')
    def _onchange_location_id(self):
        if self.location_id:
            same_location = self.search([('location_id','=',self.location_id.id)], limit=1)
            if same_location and same_location.id != self.id:
                raise UserError('Lokasi %s sudah digunakan' % self.location_id.name)
            
    @api.onchange('lot_ids')
    def _onchange_lot_ids(self):
        product_list = []
        for lot in self.lot_ids:
            product_list.append(lot.product_id.id)
        self.product_ids = product_list if product_list else False

