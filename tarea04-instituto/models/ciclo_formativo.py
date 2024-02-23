from odoo import models, fields, api

class CicloFormativo(models.Model):
    _name = 'instituto.ciclo_formativo'
    _description = 'Ciclo Formativo'

    name = fields.Char(string='Nombre', required=True)
    modulos_ids = fields.One2many('instituto.modulo', 'ciclo_ids', string='Módulos' , readonly=True )