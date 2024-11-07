# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pelicula(models.Model):
    _name = 'filmotecahugo.pelicula'
    _description = 'filmotecahugo.pelicula'

    code = fields.Char(string='Código', compute="_get_code")
    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduca el nombre")
    description = fields.Text(string="Descripción")
    film_date = fields.Date(string="Fecha")
    start_date = fields.Datetime(string="Fecha comienzo")
    end_date = fields.Datetime(string="Fecha final")
    is_spanish = fields.Boolean(string="Es española")
    image = fields.Image(String="Imagen")
    language = fields.Selection(selection=[("Es", "Español"), ("In", "Ingles"), ("De", "Aleman"), ("Fr", "Frances")],
                                string="Idioma", default="Es")
    opinion = fields.Selection(selection=[("0", "mala"), ("1", "regular"), ("2", "buena")], string="Opinion",
                               default="1")
    color = fields.Boolean(string="Color")

    # Relación entre tablas
    genero_id = fields.Many2one("filmotecahugo.genero", string="Género", required=True, ondelete="cascade")
    tecnicas_id = fields.Many2many(comodel_name="filmotecahugo.tecnica",
                                   relation="tecnicas_peliculas",
                                   column1="tecnicas_ids",
                                   column2="peliculas_ids")

    # @api.one Para recibir un único objeto
    def _get_code(self):
        for pelicula in self:
            if len(pelicula.genero_id) == 0:
                pelicula.code = "FILM_" + str(pelicula.id)
            else:
                pelicula.code = str(pelicula.genero_id.name).upper() + "_" + str(pelicula.id)
