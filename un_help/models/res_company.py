from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    un_use_boxes = fields.Boolean(default=False, string='Use Boxes')
