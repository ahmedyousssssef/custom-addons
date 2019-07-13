# -*- coding: utf-8 -*-

from openerp import api, fields, models, _
import calendar
from openerp.exceptions import UserError



class hr_payslip(models.Model):
    _inherit = 'hr.payslip'

    emp_id = fields.Char(related='employee_id.employee_id', string='Employee ID' , readonly=True)
    final_net = fields.Monetary(string="NET Salary" , compute='get_final_amounts')
    final_gross = fields.Monetary(string="Gross Salary" , compute='get_final_amounts')
    currency_id = fields.Many2one('res.currency', string='Currency', required=True,
                                  default=lambda self: self.env.user.company_id.currency_id)
    # @api.one
    # @api.depends('employee_id')
    # def get_id(self):
    #     self.emp_id = self.employee_id.id
    @api.one
    def get_final_amounts(self):
        for line in self.line_ids:
            if line.code == "NET":
                self.final_net = line.total
            if line.code == "GROSS":
                self.final_gross = line.total

