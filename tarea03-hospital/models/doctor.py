from odoo import models, fields, api

class Doctor(models.Model):

    _name = 'hospital.doctor'

    _name = 'doctor.id'

    _description = 'Doctor Model'

    name = fields.Char(string='Nombre y Apellido', required=True)
    registration_number = fields.Char(string='Número de Colegiado', required=True)