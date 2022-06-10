# Copyright 2020 VentorTech OU
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

{
    'name': 'Ventor Base',
    'version': '13.0.1.4.0',
    'author': 'VentorTech',
    'website': 'https://ventor.tech/',
    'license': 'LGPL-3',
    'installable': True,
    'images': ['static/description/main_banner.png'],
    'summary': 'Base module that allow relation between Ventor modules',
    'depends': [
        'base',
        'stock',
        'stock_picking_batch',
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/00_ir_action_server_data.xml',
        'data/ventor_option_setting.xml',
        'views/res_config.xml',
        'views/res_users.xml',
        'views/stock_inventory.xml',
        'views/stock_location.xml',
        'views/stock_picking.xml',
        'views/stock_picking_batch.xml',
        'views/stock_warehouse.xml',
        'views/ventor_option_settings.xml',
    ],
    'post_init_hook': '_post_init_hook',
}
