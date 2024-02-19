{
    'name': "A Food Delivery Management Syatem",
    'version': '1.0',
    'depends': ['base'],
    'author': "Hritik Kumar",
    'category': 'Food Delivery',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/food_delivery_views.xml',
        'views/food_delivery_menus.xml',
    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
    'application': True,
}