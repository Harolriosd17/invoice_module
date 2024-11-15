from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    # Campos adicionales para la pestaña de datos del cliente
    customer_name = fields.Char(string="Nombre del Cliente")
    customer_address = fields.Char(string="Dirección del Cliente")
    customer_email = fields.Char(string="Correo del Cliente")
    customer_city = fields.Char(string="Ciudad del Cliente")
