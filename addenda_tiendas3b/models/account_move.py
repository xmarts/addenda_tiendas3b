# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
import json

class AccountMove(models.Model):
    _inherit = "account.move"

    def test(self, v1):
        print("TEST++++++++++++++++++++++",v1)

    def total_amount(self):
        for rec in self:
            print(type(rec.tax_totals_json))
            json_string = json.loads(rec.tax_totals_json)
            print("+++",type(json_string))
            print("+++",json_string)
            amount = 0
            for ll in json_string['groups_by_subtotal'].values():
                for l in ll:
                    print("---------------------",l['tax_group_name'])
                    if l['tax_group_name'] == 'IEPS':
                        amount += l['tax_group_amount']
                        print("tax_group_amount",l['tax_group_amount'])
            amount_total = rec.amount_untaxed_signed + amount
            return amount_total

    def amount_iva(self):
        for rec in self:
            print(type(rec.tax_totals_json))
            json_string = json.loads(rec.tax_totals_json)
            print("+++",type(json_string))
            print("+++",json_string)
            amount = 0
            for ll in json_string['groups_by_subtotal'].values():
                for l in ll:
                    print("---------------------",l['tax_group_name'])
                    if l['tax_group_name'][0:3] == 'IVA':
                        amount += l['tax_group_amount']
                        print("tax_group_amount",l['tax_group_amount'])
            return amount
            