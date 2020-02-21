# -*- coding: utf-8 -*-
from odoo import models, fields, api

class consultas(models.Model):
	_name = 'sis.consultas'
	nombre = fields.Char('Nombre', size=80, required=True, help='Aqui pones el nombre')
	medico = fields.Many2one('sis.medicos', 'Médico', ondelete='restrict')
	especialidades = fields.Many2one('sis.especialidades', 'Especialidad', ondelete='restrict')

	def name_get(self):
		res = []
		for record in self:
			name = record.nombre
			res.append((record.id, name))
		return res

consultas();
