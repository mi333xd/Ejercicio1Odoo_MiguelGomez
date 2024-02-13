from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Model'

    name = fields.Char(string='Nombre y Apellido', required=True)
    sintomas = fields.Text(string='Síntomas')

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Model'

    name = fields.Char(string='Nombre y Apellido', required=True)
    registration_number = fields.Char(string='Número de Colegiado', required=True)

class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnosis Model'

    patient_id = fields.Many2one('hospital.patient', string='Paciente', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Médico', required=True)
    diagnosis_text = fields.Text(string='Diagnotico')