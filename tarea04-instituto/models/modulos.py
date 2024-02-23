from odoo import models, fields, api

class Modulo(models.Model):
    _name = 'instituto.modulo'
    _description = 'Módulo'

    name = fields.Char(string='Nombre', required=True)
    ciclo_ids = fields.Many2one('instituto.ciclo_formativo', string='Ciclo Formativo', readonly=True )
    alumnos_ids = fields.Many2many('instituto.alumno', string='Alumnos Matriculados', readonly=True )
    profesor_id = fields.Many2one('instituto.profesor', string='Profesor', readonly = True)