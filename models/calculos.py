# -*- coding: utf-8 -*-
from odoo import models, fields, api

class calculos(models.Model):
    _name = "sis.calculos"
    edad = fields.Integer(string='Edad')
    peso = fields.Integer(string='Peso')
    altura = fields.Float(string='Altura')
    imc = fields.Char(string='IMC', compute='_calcularIMC')
    dni = fields.Char(string='DNI', compute='_generaDNI')

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
                self.imc = "obesidad leve"
            elif c >= 35.00 and c <= 39.00:
                self.imc = "obesidad media"
            elif c >= 40.00:
                self.imc = "obesidad morbida"

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