# -*- coding: utf-8 -*-

from odoo import models, fields, api


class task(models.Model):
    _name = "manage.task"
    _description = "manage.task"

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripcion")
    creation_date = fields.Date()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_paused = fields.Boolean()
    sprint = fields.Many2one("manage.sprint")


class sprint(models.Model):
    _name = "manage.sprint"
    _description = "manage.sprint"

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripcion")
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    task = fields.One2many("manage.task", "sprint")
