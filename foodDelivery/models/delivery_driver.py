from odoo import models, fields

class DeliveryDriver(models.Model):
    _name = "delivery.driver"
    _description = "Delivery driver details"

    ############## Basic Properties ##############
    name = fields.Char("Name", required=True)
    phone = fields.Char("Mobile Number", required=True)
    vehicle_type = fields.Char("Vehicle")
    availability = fields.Boolean("Available", default=True)