# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pelicula(models.Model):
    _name = 'filmotecahugo.pelicula'
    _description = 'filmotecahugo.pelicula'

    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduca el nombre")
    description = fields.Text(string="Descripción")
    film_date = fields.Date(string="Fecha")
    start_date = fields.Datetime(string="Fecha comienzo")
    end_date = fields.Datetime(string="Fecha final")
    is_spanish = fields.Boolean(string="Es española")

    # Relación entre tablas
    genero_id = fields.Many2one("filmotecahugo.genero", string="Género", required=True, ondelete="cascade")
