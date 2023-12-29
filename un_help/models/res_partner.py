from odoo import api, models, fields, _
from odoo.exceptions import UserError


class Partner(models.Model):
    _inherit = 'res.partner'

    type = fields.Selection(selection_add=[('un_contact', 'UN Contact')])
    un_help_ids = fields.One2many('un.help', inverse_name='partner_id')
    age = fields.Integer()
    sex = fields.Selection([('man', 'Man'), ('woman', 'Women')])
    social_status = fields.Selection([
        ('migrant', 'Migrant'),
        ('pensioner', 'Pensioner'),
        ('spf', 'From a single-parent family'),
        ('large', 'From a large family'),
        ('disability', 'Person with a disability')],
        default='migrant',
    )
    family_members_count = fields.Integer()
    un_help_received = fields.Boolean(compute='_compute_un_help_received')

    @api.depends('un_help_ids')
    def _compute_un_help_received(self):
        current_day = fields.Date.today()
        for partner in self:
            partner.un_help_received = any(
                partner.un_help_ids.filtered(
                lambda u: u.date_received.month == current_day.month
                and u.date_received.year == current_day.year
            ))

    def action_receive_un_help(self):
        if len(self.company_id) > 1:
            raise UserError(_('Cannot receive for multiple companies. Receive UN Help for each company separately'))
        un_contacts = self.filtered(lambda partner: partner.type == 'un_contact')
        current_day = fields.Date.today()
        if any(p.un_help_received for p in un_contacts):
            raise UserError(_('Already received this month'))

        if self.env.company.un_use_boxes:
            box_ids = self.env['un.box'].search([('state', '=', 'to_consume')], limit=len(un_contacts))
            if not box_ids or len(box_ids) < len(un_contacts):
                raise UserError(_(
                    'Not enough boxes available to receive for this contact/s.' \
                    'Requested %(partners)d available %(boxes)d',
                    partners=len(un_contacts),
                    boxes=len(box_ids)
                ))
            vals = [{'partner_id': partner.id, 'date_received': current_day, 'un_box_id': box.id}
                    for partner, box in zip(un_contacts, box_ids)]
            help_ids = self.env['un.help'].create(vals)
            for help_id in help_ids:
                help_id.un_box_id.un_help_id = help_id
            box_ids.button_use()
            return {}

        vals = [{'partner_id': p.id, 'date_received': current_day} for p in un_contacts]
        self.env['un.help'].create(vals)
        return {}

    @api.ondelete(at_uninstall=False)
    def _unlink_except_boxes_locked(self):
        for partner in self:
            if partner.un_help_ids:
                box_ids = partner.un_help_ids.un_box_id
                if any(box.state == 'locked' for box in box_ids):
                    raise UserError(_('Can not delete partner with locked box'))
                if box_ids:
                    box_ids.partner_id = False
                    box_ids.button_draft()
                partner.un_help_ids.unlink()
