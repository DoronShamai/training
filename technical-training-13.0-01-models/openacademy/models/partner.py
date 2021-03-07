# -*- coding: utf-8 -*-
from odoo import fields, models


class Partner(models.Model):
    _name = 'openacademy.partner'
    _description = 'Partner'

    name = fields.Char()
    email = fields.Char()
    address = fields.Text()
    partner_type = fields.Selection([('student', 'Student'), ('lecturer', 'Lecturer')], default="student")
    session_id = fields.Many2one('openacademy.session', string="Session")

