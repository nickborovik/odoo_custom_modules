# -*- coding: utf-8 -*-
from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    phone_ids = fields.One2many('phone.phone', 'partner_id', string='Phones')
