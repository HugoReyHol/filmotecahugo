# -*- coding: utf-8 -*-

from odoo import models, fields, api


class genero(models.Model):
    _name = 'filmotecahugo.genero'
    _description = 'filmotecahugo.genero'

    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduca el nombre")
    description = fields.Text(string="Descripción")

    # Relaciones tablas
    peliculas_id = fields.One2many(string="Películas", comodel_name="filmotecahugo.pelicula", inverse_name="genero_id")
