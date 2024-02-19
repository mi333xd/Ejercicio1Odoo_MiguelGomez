
from odoo import models, fields

class HospitalDiagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'Diagnóstico'

    _paciente_id = fields.Many2one('hospital.paciente', string='Paciente')
    _doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    diagnostico = fields.Char(string='Diagnóstico')