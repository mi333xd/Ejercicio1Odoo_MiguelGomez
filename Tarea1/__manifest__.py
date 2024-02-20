# -*- coding: utf-8 -*-
{
    'name': "Tarea 1",

    'summary': "Ejercicio de la Tarea 1",

    'description': """Ejercicio de la Tarea 1 """,

    'author': "EDR",
    'category': 'Productivity',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],

}
