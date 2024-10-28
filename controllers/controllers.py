# -*- coding: utf-8 -*-
# from odoo import http


# class Filmotecahugo(http.Controller):
#     @http.route('/filmotecahugo/filmotecahugo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filmotecahugo/filmotecahugo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('filmotecahugo.listing', {
#             'root': '/filmotecahugo/filmotecahugo',
#             'objects': http.request.env['filmotecahugo.filmotecahugo'].search([]),
#         })

#     @http.route('/filmotecahugo/filmotecahugo/objects/<model("filmotecahugo.filmotecahugo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filmotecahugo.object', {
#             'object': obj
#         })
