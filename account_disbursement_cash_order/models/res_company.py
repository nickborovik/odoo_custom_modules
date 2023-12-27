from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    accountant_id = fields.Many2one('hr.employee')
    director_id = fields.Many2one('hr.employee')
    cashier_id = fields.Many2one('hr.employee')
