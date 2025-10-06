from flask import Flask
from model import Model
from controller import Controller

def criar_app():
    app = Flask(__name__, static_folder='view/static', template_folder='view/templates')
    app.config['SECRET_KEY'] = 'secret_key'


    model = Model()
    controller = Controller(model)


    app.register_blueprint(controller.controller)

    app.run(debug=True)


if __name__ == '__main__':
    criar_app()