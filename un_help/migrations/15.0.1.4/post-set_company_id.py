import logging
from odoo import api, fields, SUPERUSER_ID

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    un_help_ids = env["un.help"].search([])
    un_help_ids.company_id = env.company
