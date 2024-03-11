from odoo import models, fields


class OrderLine(models.Model):
    _name = 'food.delivery.order.line'
    _description = 'Order Line'

    order_id = fields.Many2one('food.delivery.order', string='Order')
    item_id = fields.Many2one('food.delivery.menu.item', string='Menu Item')
    quantity = fields.Integer(string='Quantity')