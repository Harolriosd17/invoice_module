{
    'name': 'Facturación Panamá',
    'version': '16.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Extiende el formulario de facturas en Odoo 16',
    'author': 'Harol Rios',
    'depends': ['account'],  # Asegúrate de que dependa del módulo de contabilidad
    'data': [
        'views/invoice_view.xml',  # Vista extendida de la factura
    ],
    'installable': True,
    'application': False,
}
