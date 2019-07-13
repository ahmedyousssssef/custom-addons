#	-*-	coding:	utf-8	-*-
from openerp import models, fields, api, _
import re
from openerp.osv import osv


class HrEmployee(models.Model):
    _inherit = 'hr.employee'


    employee_insurance_num = fields.Char(string='Social Insurance Number', copy=False, required=False)
    mobile_phone = fields.Char(string='Work Mobile', readonly=False)
    # mobile_phone = fields.D(string='Work Mobile', readonly=False)
    resignation_date = fields.Date('Resignation Date')

    def create(self,cr,uid,vals,context=None):
        if 'employee_insurance_num' in vals and vals['employee_insurance_num']:
            if re.match("^[0-9]*$", vals['employee_insurance_num']) != None:
                pass
            else:
                raise osv.except_osv(_('Invalid Social Insurance Number'), _('Please enter a valid Social Insurance Number'))
        return super(HrEmployee, self).create(cr, uid,vals, context=context)

    @api.multi
    def write(self, vals):
        if 'employee_insurance_num' in vals and vals['employee_insurance_num']:
            if re.match("^[0-9]*$", vals['employee_insurance_num']) != None:
                pass
            else:
                raise osv.except_osv(_('Invalid Social Insurance Number'), _('Please enter a valid Social Insurance Number'))
        return super(HrEmployee, self).write(vals)


