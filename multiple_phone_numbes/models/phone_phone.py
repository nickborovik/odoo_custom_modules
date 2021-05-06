# -*- coding: utf-8 -*-
from odoo import fields, models


class Phone(models.Model):
    _name = 'phone.phone'
    _description = 'Phone model'

    title = fields.Char(string='Title')
    number = fields.Char(string='Number', required=True)
    partner_id = fields.Many2one('res.partner', readonly=False, ondelete='cascade')

    def name_get(self):
        result = []
        for phone in self:
            result.append((phone.id, phone.number))
        return result
