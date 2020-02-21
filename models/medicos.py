# -*- coding: utf-8 -*-
from odoo import models, fields, api
import random

class Medicos(models.Model):
    _name = "sis.medicos"
    nombre = fields.Char(string='Nombre', required=True)
    primer_apellido = fields.Char(string='Primer Apellido', required=True)
    segundo_apellido = fields.Char(string='Segundo Apellido', required=True)
    foto = fields.Binary(string='Foto')
    edad = fields.Integer(string='Edad')
    peso = fields.Integer(string='Peso')
    altura = fields.Float(string='Altura')
    imc = fields.Char(string='IMC', compute='_calcularIMC')
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    genero = fields.Selection([('h', 'Hombre'), ('m', 'Mujer'), ('o', 'Otro')], string='Género')
    nacionalidad = fields.Many2one('sis.nacionalidades', string='Nacionalidad', ondelete='restrict')
    especialidad = fields.Many2one('sis.especialidades', 'Especialidad', ondelete='restrict')
    dni = fields.Char(string='DNI', compute='_generaDNI')
    country_id = fields.Many2one('sis.paises', 'País', ondelete='restrict')

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res

    @api.one
    @api.depends('peso', 'altura')
    def _calcularIMC(self):
        if (self.peso != 0 and self.altura != 0):
            c = (self.peso/(self.altura*2))
            if c >= 0 and c <= 15.99:
                self.imc = "Delgadez severa"
            elif c >= 16.00 and c <= 16.99:
                self.imc = "Delgadez moderada"
            elif c >= 17.00 and c <= 18.49:
                self.imc = "Delgadez leve"
            elif c >= 18.50 and c <= 24.99:
                self.imc = "Normal"
            elif c >= 25.00 and c <= 29.99:
                self.imc = "Sobrepeso"
            elif c >= 30.00 and c <= 34.99:
                self.imc = "Obesidad leve"
            elif c >= 35.00 and c <= 39.00:
                self.imc = "Obesidad media"
            elif c >= 40.00:
                self.imc = "Obesidad morbida"

    @api.one
    @api.depends('edad')
    def _generaDNI(self):
        if (self.edad != 0):
            c = random.randint(0, 100000000)
            diccionario = {0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y", 7: "F", 8: "P", 9: "D", 10: "X",
                           11: "B", 12: "N", 13: "J", 14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L",
                           20: "C", 21: "K", 22: "E"}
            resto = c % 23
            letra = diccionario[resto]
            self.dni = str(c) + letra

Medicos()