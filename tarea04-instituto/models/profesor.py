from odoo import models, fields

class Profesor(models.Model):
    _name = 'instituto.profesor'
    _description = 'Profesor'

    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido')
    dni = fields.Char(string='DNI')

    modulos_ids = fields.One2many('instituto.modulo', 'profesor_id', string='Módulos Impartidos' , readonly=True)