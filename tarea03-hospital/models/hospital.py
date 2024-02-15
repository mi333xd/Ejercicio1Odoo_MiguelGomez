from odoo import models, fields, api

class Hospital(models.Model):
    _name = 'hospital'
    _description = 'Hospital Model'

    paciente_id = fields.Many2one('paciente')
    doctor_id = fields.Many2one('doctor')
    
    diagnostico = fields.Char(string= 'Diagnostico')