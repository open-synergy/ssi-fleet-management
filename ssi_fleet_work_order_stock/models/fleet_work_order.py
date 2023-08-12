# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class FleetWorkOrder(models.Model):
    _name = "fleet_work_order"
    _inherit = ["fleet_work_order"]

    picking_type_id = fields.Many2one(
        comodel_name="stock.picking.type",
        string="Picking Type",
        required=True,
        ondelete="restrict",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
    allowed_picking_type_ids = fields.Many2many(
        comodel_name="stock.picking.type",
        string="Allowed Picking Types",
        related="type_id.allowed_picking_type_ids",
        store=False
    )
