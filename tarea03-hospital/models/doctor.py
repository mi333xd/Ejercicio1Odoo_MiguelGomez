from odoo import models, fields, api

class Doctor(models.Model):

    _name = 'hospital.doctor'

    _description = 'Doctor Model'

    name = fields.Char(string='Nombre y Apellido', required=True)
    registration_number = fields.Char(string='Número de Colegiado', required=True)