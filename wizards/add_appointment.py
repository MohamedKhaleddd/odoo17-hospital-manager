from odoo import fields,models

class AddAppointment(models.TransientModel):
    _name="add_appointment"

    patient_id= fields.Many2one('res.partner',required=True,string="Patient",
                                    
                                    domain=[('is_patient','=',True)]
                                    )

    doctor_id=fields.Many2one('res.users',required=True,string="Doctor",
                                    domain=[('is_doctor','=',True)]

    )
    note=fields.Text(string="Notes")
    app_date=fields.Datetime(required=True,string="Book Date")

    def confirm_appointment(self):
        vals={
            "patient_id":self.patient_id.id,
            "doctor_id":self.doctor_id.id,
            "note":self.note,
            "app_date":self.app_date
        }
        self.env["my_appointment"].create(vals)