from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    un_use_boxes = fields.Boolean(
        related='company_id.un_use_boxes',
        readonly=False,
    )
