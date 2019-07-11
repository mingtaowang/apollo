# -*- coding: utf-8 -*-

from flask import Flask, render_template

from apollo.config import HTTP_HOST, HTTP_PORT, DEBUG

from apollo.views.api.east.items import bp

app = Flask(__name__, template_folder='apollo/templates', static_folder='apollo/static')
app.register_blueprint(bp)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HTTP_HOST, port=HTTP_PORT)
