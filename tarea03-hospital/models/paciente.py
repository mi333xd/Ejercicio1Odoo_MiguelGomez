from odoo import models, fields, api

class Paciente(models.Model):

    _name = 'hospital.paciente'
    _description = 'Paciente Model'

    name = fields.Char(string='Nombre y Apellido', required=True)
    sintomas = fields.Char(string='Síntomas', required=True)

    _name = 'paciente'
    _description = 'Paciente Model'

    name = fields.Char(string='Nombre y Apellido', required=True)
    sintomas = fields.Char(string='Síntomas', required=True)