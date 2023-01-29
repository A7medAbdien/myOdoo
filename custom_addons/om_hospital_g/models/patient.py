import datetime

from odoo import fields, models, api


class HospitalPatient(models.Model):
    # that will create a table with name "hospital_patient"
    _name = "hospital.patientg"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient G"

    active = fields.Boolean(string="Active", default=True)
    # age = fields.Integer(string="Age", tracking=True)
    # list with tubules (key,value)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    name = fields.Char(string="Name", tracking=True)
    ref = fields.Char(string="Recreance")

    dob = fields.Date(string="Date of Birth")
    # age = fields.Integer(string="Age", tracking=True, compute='_compute_age')
    age = fields.Integer(string="Age", tracking=True, compute='_compute_age', store=True)
    appointment_id = fields.Many2one('hospital.appointmentg', 'Appointment', tracking=True)
    image = fields.Image(string='Image')
    tag_ids = fields.Many2many(
        string='Tag',
        comodel_name='patient.tagg'
    )

    @api.model
    def create(self, vals_list):
        print("Odoo Metes are the best", vals_list)
        vals_list['ref'] = 'REFERENCE'
        return super(HospitalPatient, self).create(vals_list)

    @api.depends('dob')
    def _compute_age(self):
        print("self................", self)
        for rec in self:
            today = datetime.date.today()
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 1

    @api.model
    def create(self, vals_list):
        curr_seq = self.env['ir.sequence'].next_by_code('hospital.patientg')
        print("Odoo Metes are the best", curr_seq)
        vals_list['ref'] = curr_seq
        return super(HospitalPatient, self).create(vals_list)
