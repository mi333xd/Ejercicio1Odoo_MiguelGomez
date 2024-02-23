from odoo import models, fields

class Alumno(models.Model):
    _name = 'instituto.alumno'
    _description = 'Alumno'

    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido')
    dni = fields.Char(string='DNI')
    modulos_ids = fields.Many2many('instituto.modulo', string='Módulos Matriculados', readonly=True)