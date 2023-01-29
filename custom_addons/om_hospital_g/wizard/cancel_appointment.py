import datetime

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
    date_cancel = fields.Date(string='Cancellation Date')

    @api.model
    def default_get(self, fields):
        print(datetime.date.today())
        rec = super(CancelAppointmentWizard, self).default_get(fields)
        rec['date_cancel'] = datetime.date.today()
        return rec

    def action_cancel(self):
        return
