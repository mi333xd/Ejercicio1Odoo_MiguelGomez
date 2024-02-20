# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class lista_tareas(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'lista_tareas.lista'
    _description = 'Modelo de la lista de tareas'
    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    
    tarea = fields.Char(string='Tarea', required=True)    
    imagen = fields.Image('imagen',max_width=50,max_height=50)

    prioridad = fields.Integer(string='Prioridad')
    urgente = fields.Boolean(string='Urgente', compute="_compute_urgente", store=True)
    realizada = fields.Boolean(string='Realizada')
    fecha_inicio = fields.Date(string='Fecha de inicio')
    fecha_fin = fields.Date(string='Fecha de fin')

    @api.depends('prioridad')
    def _compute_urgente(self):
        for record in self:
            record.urgente = record.prioridad > 30

    def mark_done(self):
        self.write({'realizada': True})
