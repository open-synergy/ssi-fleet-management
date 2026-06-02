# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import tagged

from odoo_yaml_test import YamlTransactionCase


@tagged("post_install", "-at_install")
class TestFleetVehicle(YamlTransactionCase):
    def test_fleet_vehicle(self):
        self.run_yaml_scenario("test_data_fleet_vehicle.yaml")
