from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    cash_order_date = fields.Date(default=fields.Date.today)
    accountant_id = fields.Many2one(
        'hr.employee', default=lambda self: self.env.company.accountant_id)
    director_id = fields.Many2one(
        'hr.employee', default=lambda self: self.env.company.director_id)
    cashier_id = fields.Many2one(
        'hr.employee', default=lambda self: self.env.company.cashier_id)
    service_name = fields.Char(translate=True)
    cash_order_partner_id = fields.Many2one('res.partner')

    def _get_coins_total(self):
        self.ensure_one()
        return str(int(round((self.amount_total - int(self.amount_total)) * 100, 2))).zfill(2)
