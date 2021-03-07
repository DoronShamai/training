from odoo import fields, models


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'

    name = fields.Char(string='Title')

    partner_ids = fields.Many2many('openacademy.partner', string="Lecturers")
