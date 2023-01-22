from odoo import models, fields


class HospitalAppointment(models.Model):
    # that will create a table with name "hospital_appointment"
    _name = "hospital.appointmentg"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment G"

    patient_id = fields.Many2one('hospital.patientg', 'Patient', tracking=True)
    appointment_time = fields.Datetime(
        string="Appointment Time", default=fields.Datetime.now, tracking=True)
    booking_date = fields.Date(
        string="Booking Date", default=fields.Date.context_today, tracking=True)
    gender = fields.Selection(related="patient_id.gender", readonly=True)

