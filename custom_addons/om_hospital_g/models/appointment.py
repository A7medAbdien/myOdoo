from odoo import models, fields, api


class HospitalAppointment(models.Model):
    # that will create a table with name "hospital_appointment"
    _name = "hospital.appointmentg"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment G"

    patient_id = fields.Many2one('hospital.patientg', 'Patient', tracking=True)
