from babel.dates import format_date
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class UnHelp(models.Model):
    _name = 'un.help'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'UN Help model'
    _order = 'date_received asc, sequence asc, id asc'

    def _get_default_color(self):
        return fields.Date.today().month - 1

    name = fields.Char(translate=True, compute='_compute_name')
    color = fields.Integer('Color Index', default=_get_default_color)
    date_received = fields.Date(required=True)
    partner_id = fields.Many2one('res.partner', required=True)
    sex = fields.Selection(related='partner_id.sex', readonly=False)
    age = fields.Integer(related='partner_id.age', readonly=False)
    social_status = fields.Selection(related='partner_id.social_status', readonly=False)
    family_members_count = fields.Integer(related='partner_id.family_members_count', readonly=False)
    note = fields.Char()
    sequence = fields.Integer(default=10)
    company_id = fields.Many2one('res.company', 'Company', index=True, default=lambda self: self.env.company)
    un_box_id = fields.Many2one('un.box', string='Box')

    @api.depends('date_received')
    def _compute_name(self):
        lang = self.env.user.lang
        for un_help in self:
            un_help.name = _('Draft')
            if un_help.date_received:
                un_help.name = format_date(
                    un_help.date_received, 'LLLL yyyy', locale=lang
                )

    @api.ondelete(at_uninstall=False)
    def _unlink_except_box_locked(self):
        for un_help in self:
            box = un_help.un_box_id
            if not box:
                continue
            if box and box.state == 'locked':
                raise UserError(_('Can not delete UN Help with locked box'))
            box.state = 'to_consume'
