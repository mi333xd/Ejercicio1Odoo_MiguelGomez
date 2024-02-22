from odoo import models, fields, api

class Doctor(models.Model):

    _name = 'hospital.doctor'

    _description = 'Doctor Model'

    name = fields.Char(string='Nombre y Apellido', required=True)
    registration_number = fields.Char(string='Número de Colegiado', required=True)
    
    _diagnosticos = fields.One2many('hospital.diagnostico', '_doctor_id', string='Diagnosticos',  readonly=True )