import os

from flask import Flask
from flask_cors import CORS

from database import mongodb
from todo_list.apis.api import todo_list_bp


def make_app():
    environment = os.environ.get("APPLICATION_ENV", "development")

    application = Flask(__name__)
    application.config.from_object("config.default")
    application.config.from_object(f"config.{environment}")

    CORS(application)

    application.register_blueprint(todo_list_bp)

    mongodb.connect(application.config["MONGO_URL"])

    return application


if __name__ == "__main__":
    app = make_app()
    app.run(host="0.0.0.0")
