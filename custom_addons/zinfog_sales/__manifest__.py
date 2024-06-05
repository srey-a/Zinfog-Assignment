# -*- coding: utf-8 -*-
{
    'name': "zinfog_sales",

    'summary': """Add a delivery charge to sale orders and invoices""",

    'description': """
        *Add a field in product master minimum cost and Brand name
        *In sale order line give the brand field and when choose product the brand field autofill
        *The unit price should not be less than the minimum cost of product
        
        *Add a new field in sale order to enter the delivery charge
        *delivery charge is 10 percentage of total amount.its auto fill in delivery charge field
        *create invoice aganist the sale order the delivery charge pass from sale order to invoice
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    # any module necessary for this one to work correctly
    'depends': ['sale', 'account','product'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/sale_order.xml',
        'views/account_move_view.xml',
        'views/product_view.xml',
        'views/sale_order_line_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
