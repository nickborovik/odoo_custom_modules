from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        invoice_vals['service_name'] = self.order_line[:1].name
        invoice_vals['cash_order_partner_id'] = self.partner_id.id
        return invoice_vals
