# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class Patients(models.Model):
    _inherit= 'res.partner'

    is_patient=fields.Boolean(string="Is Patient")
    birthday= fields.Date()
    age= fields.Integer(string="Age")
    app_count=fields.Integer(string='Count',compute="get_app_count")


    def get_appointment(self):
        action={
            'name': 'Appointment',
            'res_model':'my_appointment',
            'view_mode': 'tree,form',
            'view_id':False,
            'type': 'ir.actions.act_window',
            'domain': [('patient_id','=',self.id)]
        }
        return action

    def get_app_count(self):
        count=self.env['my_appointment'].search_count([('patient_id','=',self.id)])
        self.app_count=count


class Doctors(models.Model):
    _inherit = "res.users"
    is_doctor= fields.Boolean("Is Doctor")
    is_supervisor=fields.Boolean("Is Supervisor")

class Appointments(models.Model):
    _name="my_appointment"
    _description="Appointement model"
    _inherit=['mail.thread','mail.activity.mixin']

    name= fields.Char(string="Appointement id",readonly=True,index=True,copy=False,
                        required=True,default=lambda self: _('New'))

    patient_id=fields.Many2one('res.partner',domain=[('is_patient','=',True)],
                            string="patient",required=True)

    patient_age=fields.Integer("Age",related='patient_id.age')

    note=fields.Text(string="Notes")
    app_date=fields.Datetime(required=True,string="Appointement Date")

    state= fields.Selection([('draft','Draft'),
                            ('confirm','Confirm'),
                            ('done','Done'),
                            ('cancel','Cancel')],string='Status',readonly=True,default='draft')
    doctor_notes=fields.Text(string="Doctor Notes")
    doctor_id=fields.Many2one('res.users',string="Doctor",domain=[('is_doctor','=',True)])
    predescription_id=fields.One2many('predescription','appointment_id')

    @api.model
    def create(self,vals):
        if vals.get('name',_('New')) == _('New'):
            vals['name']=self.env['ir.sequence'].next_by_code('my_appointment.sequence') or _('New')
        result = super(Appointments,self).create(vals)
        return result

    def get_draft(self):
        self.state='draft'

    def get_confirm(self):
        self.state='confirm'

    def get_done(self):
        self.state='done'

    def get_cancel(self):
        self.state='cancel'


class Predescription(models.Model):
    _name='predescription'
    name=fields.Char(string="Medicine name")
    notes=fields.Text(string="Notes")
    appointment_id=fields.Many2one('my_appointment',string='Appointments')
    medicine_id=fields.Many2one('medicines',string="Medicine")

class Medicine(models.Model):
    _name="medicines"
    name= fields.Char(string="Medicine Name")
    effective_material=fields.Char(string="Effective Material")
    predescription_id=fields.One2many('predescription','medicine_id')
