from odoo import models, fields

class Restaurant(models.Model):
    _name = 'food.delivery.restaurant'
    _description = 'Restaurant'

    name = fields.Char(string='Name', required=True)
    restaurant_address = fields.Char(string='Address')
    phone_no = fields.Char(string='Phone Number')
    email = fields.Char(string="Email")
    zipcode = fields.Char(string="Zip Code")