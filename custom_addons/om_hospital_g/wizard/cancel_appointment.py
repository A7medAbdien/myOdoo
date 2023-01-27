from odoo import api, fields, models


class CancelAppointmentWizard(models.TransientModel):
    _name = 'cancel.appointmentg.wizard'
    _description = 'Cancel Appointment Wizard'

    appointment_id = fields.Many2one(
        string='Appointment',
        comodel_name='hospital.appointmentg'
    )
    reason = fields.Text(
        string='Reason',
    )

    def action_cancel(self):
        return