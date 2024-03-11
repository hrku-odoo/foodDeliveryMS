from odoo import models, fields

class Delivery(models.Model):
    _name = 'food.delivery.delivery'
    _description = 'Delivery'

    order_id = fields.Many2one('food.delivery.order', string='Order')
    driver_id = fields.Many2one('food.delivery.driver', string='Driver')
    delivery_status = fields.Selection([('pending', 'Pending'), ('delivered', 'Delivered')], string='Delivery Status')
    delivery_date = fields.Datetime(string='Delivery Date')