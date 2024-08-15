# -*- coding: utf-8 -*-
{
    'name': "eLearning CUJAE",

    'summary': """
        Modulo elearning Cujae
        """,
    'sequence': 1,

    'description': """
        Este módulo es para impartir cursos digitales
    """,

    'author': "Reinaldo y Keila",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website/eLearning',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_slides','survey','website_slides_survey'],

    # always loaded
    'data': [        
        'views/survey_question.xml',
        #'static/description/icon.png',
        'views/slide_slide_views.xml',
        'views/survey_survey_views.xml',
        #'views/res_config_settings_views.xml',
        'views/website_slides_menu_views.xml',
        'views/website_slide_templates_course.xml',
        'views/website_slides_templates_lesson.xml',
        'views/website_slides_templates_utils.xml',
        'views/website_slides_templates_lesson_fullscreen.xml',
        'views/website_slides_templates_homepage.xml',
        'views/website_profile.xml',
        'views/survey_templates.xml',
        'security/security.xml'
        
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/account_move_demo.xml',
    ],

    # 'assets': {
     'web.assets_tests': [
        'elearning_cujae/static/src/xml/website_slides_upload.xml',
        'elearning_cujae/static/src/xml/website_slides_fullscreen.xml',

     ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
