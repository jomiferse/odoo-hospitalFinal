# -*- coding: utf-8 -*-
from odoo import models, fields, api

class nacionalidades(models.Model):
	_name = 'sis.nacionalidades'
	nombre = fields.Char('Nacionalidad', size=80, required=True, help='Aqui pones la nacionalidad')

	def name_get(self):
		res = []
		for record in self:
			name = record.nombre
			res.append((record.id, name))
		return res

nacionalidades();
