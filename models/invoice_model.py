# models/account_move.py
from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    # Campos nuevos para la pestaña Panamá
    panama_nombre_cliente = fields.Char(string="Nombre Cliente")
    panama_direccion = fields.Char(string="Dirección")
    panama_telefono = fields.Char(string="Teléfono")
    panama_ciudad = fields.Char(string="Ciudad")
