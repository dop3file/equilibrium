from flask import Flask, render_template, request


app = Flask(__name__)


class Webpage:
    def __init__(self, name_webpage):
        self.name_webpage = name_webpage

    def create_webpage(self):
        @app.route(self.name_webpage)
        def index():
            return 'DD'

        app.run(debug=False)

class Site:
    def __init__(self):
        pass

    def create_webpage(self, name_webpage):
        @app.route(name_webpage)
        def index():
            return 'WATAFUK'

        app.run(debug=False)


wb1 = Webpage('/')
wb1.create_webpage()
wb2 = Webpage('/dfd')
wb2.create_webpage()


