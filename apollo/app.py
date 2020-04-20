# -*- coding: utf-8 -*-

import sys

from flask import Flask
from werkzeug.utils import import_string

reload(sys).setdefaultencoding('utf-8')

blueprints = [
    'apollo.views.home:bp',
    'apollo.views.api.east.items:bp',
]


def create_app(config=None):
    app = Flask(__name__)

    for blueprint in blueprints:
        blueprint = import_string(blueprint)
        app.register_blueprint(blueprint)

    return app
