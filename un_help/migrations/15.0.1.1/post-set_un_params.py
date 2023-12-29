import logging
from odoo import api, fields, SUPERUSER_ID

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    un_contacts = env["res.partner"].search([("type", "=", "un_contact")])
    un_contacts.un_help_ids.color = 5
    un_contacts.parent_id = False
