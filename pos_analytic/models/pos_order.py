from odoo import models


class PosOrder(models.Model):
    _inherit = "pos.order"

    def _prepare_invoice_line(self, line):
        res = super()._prepare_invoice_line(line)
        analytic_account_id = line.order_id.session_id.config_id.account_analytic_id
        if analytic_account_id:
            res.update({"analytic_account_id": analytic_account_id.id})
        return res

    def action_pos_order_invoice(self):
        ctx = self.with_context(pos_analytic=True)
        return super(PosOrder, ctx).action_pos_order_invoice()
