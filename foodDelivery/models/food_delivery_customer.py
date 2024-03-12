from odoo import models, fields


class Customer(models.Model):
    _name = 'food.delivery.customer'
    _description = 'Customer'

    customer_name = fields.Char(string='Name', required=True)
    customer_address = fields.Char(string='Address')
    contact_info = fields.Char(string='Contact Information')
    email = fields.Char(string="Email")