# -*- coding: utf-8 -*-
from odoo import models, fields, api

class especialidades(models.Model):
	_name = 'sis.especialidades'
	nombre = fields.Char('Nombre', size=80, required=True, help='Aqui pones el nombre')

	def name_get(self):
		res = []
		for record in self:
			name = record.nombre
			res.append((record.id, name))
		return res

especialidades();
