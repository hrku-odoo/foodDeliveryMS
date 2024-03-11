from odoo import models, fields

class MenuItem(models.Model):
    _name = 'food.delivery.menu.item'
    _description = 'Menu Item'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price')
    restaurant_id = fields.Many2one('food.delivery.restaurant', string='Restaurant')