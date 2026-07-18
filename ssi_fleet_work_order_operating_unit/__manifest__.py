# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Fleet Work Order + Operating Unit",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "contributors": [
        "Andhitia Rama <andhitia.r@gmail.com>",
    ],
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_fleet_work_order",
        "ssi_operating_unit_mixin",
    ],
    "data": [
        "security/res_group/fleet_work_order.xml",
        "security/ir_rule/fleet_work_order.xml",
        "view/fleet_work_order.xml",
    ],
}
