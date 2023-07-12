# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval, test_python_expr


class FleetWorkOrderRouteTemplate(models.Model):
    _name = "fleet_work_order_route_template"
    _description = "Fleet Work Order Route Template"
    _inherit = ["mixin.master_data"]

    route_ids = fields.One2many(
        comodel_name="fleet_work_order_route_template.route",
        inverse_name="template_id",
        string="Routes"
    )
    location_selection_method = fields.Selection(
        selection=[
            ("manual", "Manual"),
            ("domain", "Domain")
        ],
        string="Location Selection Method",
        required=True
    )
    location_ids = fields.Many2many(
        comodel_name="res.partner",
        relation="rel_fleet_wo_type_2_location",
        column1="type_id",
        column2="location_id",
        string="Locations"
    )
    location_domain = fields.Text(
        string="Location Domain",
        default=[]
    )
    allowed_location_ids = fields.Many2many(
        comodel_name="res.partner",
        compute="_compute_allowed_location_ids",
        store=False,
        string="Allowed Locations"
    )

    @api.depends("location_selection_method", "location_ids", "location_domain")
    def _compute_allowed_location_ids(self):
        for record in self:
            result = []
            if record.location_selection_method == 'manual':
                result = record.location_ids.ids
            elif record.location_selection_method == 'domain':
                criteria = safe_eval(record.location_domain, {})
                result = self.env['res.partner'].search(criteria).ids
            record.allowed_location_ids = result
