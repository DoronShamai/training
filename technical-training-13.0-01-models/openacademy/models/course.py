from odoo import fields, models


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'

    name = fields.Char(string='Title')

    lecturer_ids = fields.Many2many('openacademy.partner', string="Lecturers")
    student_ids = fields.Many2many('openacademy.partner', string='Students')
