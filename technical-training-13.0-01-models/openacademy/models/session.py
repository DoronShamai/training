from odoo import fields, models


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Session'

    name = fields.Char(string='Title')
    semester = fields.Selection([('semester A', 'Semester A'), ('semester B', 'Semester B')], default="semester A")
    duration = fields.Integer(3)
    
    start_time = fields.Datetime()
    start_date = fields.Date()
    
    lecturer_ids = fields.Oney2many('openacademy.partner', string="Lecturers")
    student_ids = fields.Many2one('openacademy.partner', string='Students')
