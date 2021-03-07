# -*- coding: utf-8 -*-
from odoo import fields, models


class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title')

    author_ids = fields.Many2many("library.partner", string="Authors")
    edition_date = fields.Date()
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one('library.publisher', string='Publisher')

    # why Onw2many? rental_id - > book_ids, maybe the name of rental_ids is missguided
    rental_ids = fields.One2many('library.rental', 'book_id', string='Rentals')
