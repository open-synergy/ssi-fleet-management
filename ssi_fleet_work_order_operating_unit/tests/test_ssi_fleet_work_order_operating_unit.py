# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestSSIFleetWorkOrderOperatingUnit(YamlTransactionCase):
    def test_ssi_fleet_work_order_operating_unit(self):
        self.run_yaml_scenario("test_data_ssi_fleet_work_order_operating_unit.yaml")
