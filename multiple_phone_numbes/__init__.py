# -*- coding: utf-8 -*-
import logging
from . import models

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)


def _copy_mobile_and_phone_numbers(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    _logger.info('Create phones from existing "phone" and "mobile" fields')
    partners = env['res.partner'].search([])
    Phone = env['phone.phone']
    vals = []
    for partner in partners:
        if partner.phone:
            vals.append({'number': partner.phone, 'title': 'phone', 'partner_id': partner.id})
        if partner.mobile:
            vals.append({'number': partner.mobile, 'title': 'mobile', 'partner_id': partner.id})
    if vals:
        phones = Phone.create(vals)
    _logger.info('%s records created' % len(phones))
