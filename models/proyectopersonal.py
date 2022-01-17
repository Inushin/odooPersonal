from odoo import models, fields, api

class AreaDescanso(models.Model):
    _name = 'almi_personal_area_descanso'
    _description = 'Areas de descanso'

    name=fields.Char('Nombre')
    aforo=fields.Integer('Aforo')
    maquinas_vending=fields.Many2many('almi_personal_maquina', string='Máquinas disponibles')
#    maquinas_vending=fields.Char('Máquinas de Vending')
    seccion_fabrica=fields.Selection([('prod','Producción'),('gest','Gestión'),('ing','Ingeniería')],'Sección')


class Maquina(models.Model):
    _name = 'almi_personal_maquina'
    _description = 'Maquina'


    name=fields.Char('Código')
    tipo=fields.Selection([('cafe','Café'),('comida','Comida'),('refrescos','Refrescos')],'Tipo')
    proveedor = fields.Many2one('res.partner', string="Proveedor")
    productos = fields.Many2many('almi_personal_producto_vending', string="Productos")
    fecha_revision=fields.Date('Revision')


