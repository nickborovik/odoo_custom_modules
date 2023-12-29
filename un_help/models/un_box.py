from odoo import _, api, fields, models
from odoo.exceptions import UserError


class UnBox(models.Model):
    _name = 'un.box'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Un Box model'
    _order = 'date_received asc, id asc'

    name = fields.Char(string='Name')
    un_help_id = fields.Many2one('un.help', string='UN Help')
    partner_id = fields.Many2one('res.partner', related='un_help_id.partner_id', string='UN Contact')
    date_received = fields.Date(required=True, default=fields.Date.today(), tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('to_consume', 'To Consume'),
        ('used', 'Used'),
        ('locked', 'Locked'),
        ('scrapped', 'Scrapped')
    ], default='draft', required=True, tracking=True)
    company_id = fields.Many2one('res.company', 'Company', index=True, default=lambda self: self.env.company, tracking=True)

    def button_draft(self):
        self.filtered(lambda b: b.state not in ['draft']).state = 'draft'

    def button_to_consume(self):
        self.filtered(lambda b: b.state not in ['to_consume', 'used', 'scrapped']).state = 'to_consume'

    def button_use(self):
        self.filtered(lambda b: b.state in ['draft', 'to_consume']).state = 'used'

    def button_scrap(self):
        self.state = 'scrapped'

    def button_lock(self):
        self.write({'state': 'locked'})

    def button_unlock(self):
        self.write({'state': 'used'})

    @api.ondelete(at_uninstall=False)
    def _unlink_except_box_locked(self):
        if any(box.state == 'locked' for box in self):
            raise UserError(_('Can not delete locked box'))

