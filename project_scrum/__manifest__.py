# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# Enlight.me 2020 (<https://enlightme.biz/>)

{
    'name': 'Project - Scrum',
    'category': "Project",
    'summary': 'Adds the ability to create Sprints and Scrum teams.',
    'website': 'https://enlightme.biz/',
    'version': '13.0.0.0.0',
    'license': 'AGPL-3',
    'description': """
Project Scrum
=============

This module allows you to organize your tasks with the Scrum methodology.

Using sprints, you can easily plan when your tasks should be done.

-------------

Organize your project and tasks with the Scrum methodology
----------------------------------------------------------

- Create Sprints to manage your task deadlines.
- Manage multiple sprint durations with the possibility of creating different Scrum Teams.

Focus on your business, we keep IT running

----------------------

About Enlight.me
===============

Enlight.me We are a startup working toward the large adoption of location intelligence technologies by small businesses.

Our mission is to develop community driven  platforms to democratize access to open geospatial datasets and build useful use cases for Business

Our values : Openness, Use case driven, Community empowerement.

https://enlightme.biz

----------------------

About Niboo
===========

Niboo is a technology company, specialized in developing business solutions to your needs. 
Niboo combines expertise in both IT and management consulting. As an active partner in the Odoo Community, 
Niboo also contributes to the evolution of open-source business solutions.

http://www.niboo.be/page/contactus

        """,
    'author': 'Enlight.me - Niboo',
    'depends': ['project'],
    'data': [
        'views/project_view.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [],
    'images': [
        'static/description/project_scrum_cover.png',
    ],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': False,
}
