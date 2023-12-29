from odoo import api, fields, models


class UnBox(models.TransientModel):
    _name = 'receive.un.box'
    _description = 'Receive Un Box wizard'

    box_name = fields.Char()
    box_count = fields.Integer(required=True)
    date_received = fields.Date(required=True, default=fields.Date.today())
    state = fields.Selection([
        ('draft', 'Draft'),
        ('to_consume', 'To Consume'),
        ('used', 'Used'),
        ('scrapped', 'Scrapped')
    ], default='draft', required=True)

    def action_receive_boxes(self):
        self.env['un.box'].create([{
            'name': (self.box_name or 'box date ' + str(self.date_received)) + ' ' + str(i),
            'date_received': self.date_received,
            'state': self.state
        } for i in range(self.box_count)])
        return {}
