from odoo import models, fields

class DeliveryDriver(models.Model):
    _name = 'food.delivery.driver'
    _description = 'Delivery Driver'

    name = fields.Char(string='Name', required=True)
    contact_info = fields.Char(string='Contact Information')