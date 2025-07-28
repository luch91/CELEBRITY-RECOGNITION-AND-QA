from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    template_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
    static_path = os.path.join(os.path.dirname(__file__), '..', 'static')

    app = Flask(__name__, template_folder=template_path, static_folder=static_path)

    app.secret_key = os.getenv("SECRET_KEY", "default_secret")

    from app.routes import main
    app.register_blueprint(main)

    return app
