from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # define api routes here..
    return app