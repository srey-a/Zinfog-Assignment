from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_charge = fields.Float(string='Delivery Charge',compute='_compute_delivery_charge', store=True)

    @api.depends('amount_total')
    def _compute_delivery_charge(self):
        for order in self:
            order.delivery_charge = order.amount_total * 0.10

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['delivery_charge'] = self.delivery_charge
        return invoice_vals
