from odoo import models, fields

class HmsPatient(models.Model):
    _name = "hms.patient"

    Firstname = fields.Char()
    Lastname = fields.Char()
    Birthdate = fields.Date()
    History = fields.Html()
    CRRatio = fields.Float()
    Blood = fields.Selection([
        ("O","O blood"),
        ("A", "A blood"),
        ("B", "B blood"),
    ])
    PCR = fields.Boolean()
    Image = fields.Binary()
    Address = fields.Text()
    Age = fields.Integer()