from odoo import _, api, fields, models


class Employee(models.Model):
    _inherit = 'hr.employee'

    initials = fields.Char(translate=True)
