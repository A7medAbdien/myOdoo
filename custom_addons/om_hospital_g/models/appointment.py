from odoo import models, fields, api


class HospitalAppointment(models.Model):
    # that will create a table with name "hospital_appointment"
    _name = "hospital.appointmentg"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment G"
    _rec_name = "patient_id"

    patient_id = fields.Many2one('hospital.patientg', 'Patient', tracking=True)
    appointment_time = fields.Datetime(
        string="Appointment Time", default=fields.Datetime.now, tracking=True)
    booking_date = fields.Date(
        string="Booking Date", default=fields.Date.context_today, tracking=True)
    gender = fields.Selection(related="patient_id.gender", readonly=True)

    ref = fields.Char(string="Reference")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
