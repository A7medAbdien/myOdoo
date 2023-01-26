from odoo import models, fields, api


class HospitalAppointment(models.Model):
    # that will create a table with name "hospital_appointment"
    _name = "hospital.appointmentg"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment G"
    _rec_name = "ref"

    patient_id = fields.Many2one('hospital.patientg', 'Patient', tracking=True)
    appointment_time = fields.Datetime(
        string="Appointment Time", default=fields.Datetime.now, tracking=True)
    booking_date = fields.Date(
        string="Booking Date", default=fields.Date.context_today, tracking=True)
    gender = fields.Selection(related="patient_id.gender", readonly=True)

    ref = fields.Char(string="Reference")
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')
    ], string='Priority')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], string='Status')
    doctor_id = fields.Many2one('res.users', string='Doctor')
    pharmacy_lines_id = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Lines')
    hide_sales_price = fields.Boolean(string='Hide Sales Price')

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print('test!!!!!!!!!!!!!!!!!!!!')
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Printed',
                'type': 'rainbow_man',
            }
        }

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
        # action = self.env.ref(
        #     'om+hospital_g.action_cancel_appointment_wizard').read()[0]
        # return action


class AppointmentPharmacyLines(models.Model):
    _name = 'appointmentg.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default=1)
    appointment_id = fields.Many2one(
        'hospital.appointmentg', string='Appointment')
