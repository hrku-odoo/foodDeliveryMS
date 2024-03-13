from odoo import models, fields, api

class Order(models.Model):
    _name = 'food.delivery.order'
    _description = 'Order'

    name = fields.Many2one('food.delivery.customer', string='Customer')
    restaurant_id = fields.Many2one('food.delivery.restaurant', string='Restaurant')
    total_price = fields.Float(string='Total Price', compute='_compute_total_price', store=True, readonly=True)
    order_date = fields.Date(string='Order Date')
    order_line_ids = fields.One2many('food.delivery.order.line', 'order_id', string='Order Lines')

    
    # Define a computed field to dynamically compute domain for order_line_ids
    @api.depends('restaurant_id')
    def _compute_order_line_domain(self):
        for order in self:
            order.order_line_domain = [('restaurant_id', '=', order.restaurant_id.id)]

    # Define a related field to store the computed domain
    # order_line_domain = fields.Char(compute='_compute_order_line_domain', store=True)

    # Override the default domain of order_line_ids with the computed domain
    # order_line_ids = fields.One2many('food.delivery.order.line', 'order_id', string='Order Lines', domain=lambda self: eval(self.order_line_domain))

    # @api.depends('order_line_ids')
    # def _compute_total_price(self):
    #     for order in self:
    #         total_price = sum(order_line.price for order_line in order.order_line_ids)
    #         order.total_price = total_price