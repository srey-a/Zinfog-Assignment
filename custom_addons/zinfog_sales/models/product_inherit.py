from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    minimum_cost = fields.Float(string="Minimum Cost")
    brand_name = fields.Char(string="Brand Name")

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    brand_name = fields.Char(string="Brand")

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.brand_name = self.product_id.product_tmpl_id.brand_name

    @api.constrains('price_unit')
    def _check_minimum_cost(self):
        for line in self:
            if line.product_id and line.price_unit < line.product_id.product_tmpl_id.minimum_cost:
                raise ValidationError(
                    _('The unit price cannot be less than the minimum cost for the product: %s' % line.product_id.name)
                )
