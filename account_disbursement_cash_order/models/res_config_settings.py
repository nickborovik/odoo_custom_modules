from odoo import _, api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    accountant_id = fields.Many2one(
        'hr.employee', readonly=False, related='company_id.accountant_id')
    director_id = fields.Many2one(
        'hr.employee', readonly=False, related='company_id.director_id')
    cashier_id = fields.Many2one(
        'hr.employee', readonly=False, related='company_id.cashier_id')
