from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    account_analytic_id = fields.Many2one(
        comodel_name="account.analytic.account", string="Analytic Account"
    )
