# -*- coding: utf-8 -*-
import datetime

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

    def toggle_color(self):
        self.color = not self.color

    def f_create(self):
        pelicula = {
            "name": "Prueba ORM",
            "color": True,
            "genero_id": 1,
            "start_date": str(datetime.date(2022, 8, 8))
        }
        print(pelicula)
        self.env['filmotecahugo.pelicula'].create(pelicula)

    def f_search(self):
        p = self.env['filmotecahugo.pelicula'].search([('color', '=', True)], limit=1)
        # p.write({'color': False})
        p.color = False

    def f_delete(self):
        self.env['filmotecahugo.pelicula'].search([('name', '=', 'borrar')], limit=1).unlink()
