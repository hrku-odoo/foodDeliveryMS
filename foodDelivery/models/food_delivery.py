from odoo import models, fields

class Restaurants(models.Model):
    _name = "food.delivery"
    _description = "This is a Restaurants list"


    ################ Basic Properties #################
    # restaurant_id = fields.

    name = fields.Char("Restaurant Name", required=True)
    address = fields.Text("Location", required=True)
    postcode = fields.Integer("Zip Code", required=True)
    cuisine_type = fields.Selection( selection=[
        ("cafeteria", "Cafeteria"),
        ("french_cuisine", "French Cuisine"),
        ("italian_cuisine", "Italian Cuisine"),
        ("buffet", "Buffet"),
    ],string="Cusine Type")