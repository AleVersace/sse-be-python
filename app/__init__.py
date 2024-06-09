from flask import Flask

from app.sse.sse import sse_bp


def create_app():
    # create and configure the app
    app = Flask(__name__)

    app.register_blueprint(sse_bp)

    return app
