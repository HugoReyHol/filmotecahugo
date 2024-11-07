from odoo import models, fields, api


class tecnica(models.Model):
    _name = 'filmotecahugo.tecnica'
    _description = 'filmotecahugo.tecnica'

    name = fields.Char(string="nombre")
    description = fields.Text(string="Descripción")

    photo = fields.Image(string="Image")

    # Relación entre tablas
    peliculas_id = fields.Many2many(comodel_name='filmotecahugo.pelicula',
                                   relation='tecnicas_peliculas',
                                   column1="peliculas_ids",
                                   column2="tecnicas_ids")
