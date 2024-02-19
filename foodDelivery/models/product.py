from odoo import models, fields

class Product(models.Model):
    _name = "products"
    _description = "Desciption of the food item"


    ################## Basic Properties ######################
    name = fields.Char("Dish Name",required=True)
    description = fields.Text("Descrfiption")
    price = fields.Integer("Price",required=True)
    available = fields.Boolean("Available", required=True)
    