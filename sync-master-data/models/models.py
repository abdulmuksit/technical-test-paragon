# -*- coding: utf-8 -*-

import json
import requests
from odoo import models, fields, api
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def sync_to_apps(self):
        for product in self:
            data = {
                'name': product.name,
                'default_code': product.default_code,
                'list_price': product.list_price,
                'standard_price': product.standard_price,
                'qty_available': product.qty_available,
            }

            url = 'https://api.apps.com/sync-product'
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer YOUR_API_KEY',
            }

            try:
                response = requests.post(url, data=json.dumps(data), headers=headers)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                raise UserError(f"Failed to sync with Z application: {str(e)}")

    @api.model
    def create(self, vals):
        product = super(ProductTemplate, self).create(vals)
        product.sync_to_apps()
        return product

    def write(self, vals):
        result = super(ProductTemplate, self).write(vals)
        self.sync_to_apps()
        return result

    def unlink(self):
        for product in self:
            product.sync_to_apps()
        return super(ProductTemplate, self).unlink()
