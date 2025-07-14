import os
from flask import Flask
from api.views.index import index

class App(Flask):
    def __init__(self, name):
        super().__init__(name)
        self.static_folder = '../static'
        self.template_folder = '../templates'
        self.secret_key = os.environ.get('SECRET_KEY')
        self._register_blueprints()

    def _register_blueprints(self):
        self.register_blueprint(index)

app = App(__name__)

if __name__ == '__main__':
    app.debug = True
    app.run()
