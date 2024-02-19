from odoo import models, fields, api

class lista_tareas(models.Model):
    _name = 'lista_tareas.lista'
    _description = 'Modelo de la lista de tareas'

    imagen = fields.Binary(string='Imagen')
    tarea = fields.Char(string='Tarea', required=True)
    prioridad = fields.Integer(string='Prioridad')
    urgente = fields.Boolean(string='Urgente', compute="_compute_urgente", store=True)
    realizada = fields.Boolean(string='Realizada')
    fecha_inicio = fields.Date(string='Fecha de inicio')
    fecha_fin = fields.Date(string='Fecha de fin')

    # Método para calcular el campo "urgente" basado en la prioridad
    @api.depends('prioridad')
    def _compute_urgente(self):
        for record in self:
            record.urgente = record.prioridad > 30

    # Método para marcar una tarea como realizada
    def mark_done(self):
        self.write({'realizada': True})