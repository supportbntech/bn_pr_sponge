from odoo import api, models, fields


class BNResCompany(models.Model):
    _inherit = "res.company"

    bank_details_main = fields.Text('Bank Details Main Currency')
    bank_details_secondary = fields.Text('Bank Details Secondary Currency')