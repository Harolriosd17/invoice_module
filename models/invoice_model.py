# models/account_move.py
from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    panama_nombre_cliente = fields.Char('Nombre del Cliente', copy=False)
    panama_direccion_cliente = fields.Char('Dirección', copy=False)
    panama_telefono_cliente = fields.Char('Teléfono', copy=False)
    panama_ciudad_cliente = fields.Char('Ciudad', copy=False)

