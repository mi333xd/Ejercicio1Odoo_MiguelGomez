
from odoo import models, fields

class HospitalDiagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'Diagnóstico'

    _paciente_id = fields.Many2one('hospital.paciente', string='Paciente')
    _doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    diagnostico = fields.Char(string='Diagnóstico')

from odoo import models, fields, api

class Hospital(models.Model):
    _name = 'hospital'
    _description = 'Hospital Model'

    paciente_id = fields.Many2one('paciente')
    doctor_id = fields.Many2one('doctor')
    
    diagnostico = fields.Char(string= 'Diagnostico')