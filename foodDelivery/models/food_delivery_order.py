from odoo import models, fields

class Order(models.Model):
    _name = 'food.delivery.order'
    _description = 'Order'

    customer_id = fields.Many2one('food.delivery.customer', string='Customer')
    restaurant_id = fields.Many2one('food.delivery.restaurant', string='Restaurant')
    total_price = fields.Float(string='Total Price')
    order_date = fields.Date(string='Order Date')
    order_line_ids = fields.One2many('food.delivery.order.line', 'order_id', string='Order Lines')