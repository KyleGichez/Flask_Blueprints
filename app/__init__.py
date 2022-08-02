from flask import Flask
from app.views.auth.auth import auth

def create_app():
    app = Flask(__name__)
    app.secret_key = "SexyMsDollarBaby"
    app.register_blueprint(auth, url_prefix = ('/'))

    return app