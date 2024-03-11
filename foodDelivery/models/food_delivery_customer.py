from odoo import models, fields


class Customer(models.Model):
    _name = 'food.delivery.customer'
    _description = 'Customer'

    name = fields.Char(string='Name', required=True)
    address = fields.Char(string='Address')
    contact_info = fields.Char(string='Contact Information')