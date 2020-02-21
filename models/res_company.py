# -*- coding: utf-8 -*-
from odoo import models, fields, api

class res_partner(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'
	rut = fields.Char('Rut' , size=10 , help='Este es rut')
	edad = fields.Integer('Edad', size=3, help='Aqui pones la edad')
	profesion = fields.Char('Profesion' , size=10 , help='Este es rut')

res_partner()