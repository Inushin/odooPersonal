# -*- coding: utf-8 -*-
# from odoo import http


# class Almi-proyecto-personal(http.Controller):
#     @http.route('/almi-proyecto-personal/almi-proyecto-personal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almi-proyecto-personal/almi-proyecto-personal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('almi-proyecto-personal.listing', {
#             'root': '/almi-proyecto-personal/almi-proyecto-personal',
#             'objects': http.request.env['almi-proyecto-personal.almi-proyecto-personal'].search([]),
#         })

#     @http.route('/almi-proyecto-personal/almi-proyecto-personal/objects/<model("almi-proyecto-personal.almi-proyecto-personal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almi-proyecto-personal.object', {
#             'object': obj
#         })
