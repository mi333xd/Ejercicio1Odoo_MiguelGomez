from odoo import models, fields

class HospitalDiagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'Diagnóstico Information'

    _paciente_id = fields.Many2one('hospital.paciente', string='Paciente')
    _doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    diagnostico = fields.Text(string='Diagnóstico' 
    )
