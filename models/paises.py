# -*- coding: utf-8 -*-
from odoo import models, fields, api

class paises(models.Model):
	_name = 'sis.paises'
	nombre = fields.Char('País', size=80, required=True, help='Aqui pones el país')

	def name_get(self):
		res = []
		for record in self:
			name = record.nombre
			res.append((record.id, name))
		return res

paises();
