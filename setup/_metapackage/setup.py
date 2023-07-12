import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-fleet-management",
    description="Meta package for open-synergy-ssi-fleet-management Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_fleet_management',
        'odoo14-addon-ssi_fleet_work_order',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
