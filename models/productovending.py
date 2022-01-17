from odoo import models, fields, api

class ProductoVending(models.Model):
    _name = 'almi_personal_producto_vending'
    _description = 'Producto Vending'

    name=fields.Char('Nombre')
    descripcion=fields.Html('Descripcion',sanitize=True, strip_style=True, translate=True)
    tipo=fields.Selection([('comida','Comida'),('bebida','Bebida')],'Tipo')
    sano=fields.Selection([('si','Sí'),('no','No')],'¿Es sano?')
    precio=fields.Float('Precio')
    

