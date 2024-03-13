from odoo import fields, models

class FoodDeliveryMenuTag(models.Model):
    _name = "food.delivery.menu.tag"
    _description = "Menu Tags"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]
    _order = "name"

    name = fields.Char("Name", required=True)
    color = fields.Integer("Color Index")
