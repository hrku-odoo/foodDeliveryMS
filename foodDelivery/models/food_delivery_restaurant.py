from odoo import models, fields

class Restaurant(models.Model):
    _name = 'food.delivery.restaurant'
    _description = 'Restaurant'

    name = fields.Char(string='Name', required=True)
    address = fields.Char(string='Address')
    contact_info = fields.Char(string='Contact Information')