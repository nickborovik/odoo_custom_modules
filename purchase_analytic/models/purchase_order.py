from odoo import _, api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    shared_analytic_account_id = fields.Many2one('account.analytic.account')

    @api.onchange('shared_analytic_account_id')
    def _onchange_shared_analytic_account_id(self):
        shared_analytic = self.shared_analytic_account_id
        self.order_line.account_analytic_id = shared_analytic if shared_analytic else False
