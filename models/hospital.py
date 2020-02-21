# -*- coding: utf-8 -*-
from odoo import models, fields, api

class hospital(models.Model):
	_name = 'sis.hospital'
	nombre = fields.Char('Nombre', size=80, required=True, help='Aqui pones el nombre')
	country_id = fields.Many2one('sis.paises', 'País', ondelete='restrict')
	consultas = fields.Many2one('sis.consultas', string='Consultas', ondelete='restrict')

	def name_get(self):
		res = []
		for record in self:
			name = record.nombre
			res.append((record.id, name))
		return res

hospital();
