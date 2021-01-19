from flask import Flask, render_template, request


app = Flask(__name__)


class Site:
    def __init__(self):
        pass

    def create_webpage(self, name_webpage):
        @app.route(name_webpage)
        def index():
            return 'WATAFUK'

        app.run(debug=False)


site = Site()
site.create_webpage('/')


