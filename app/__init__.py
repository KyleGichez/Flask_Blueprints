from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

import logging, sys

from .config import config_options
from .extensions import register_extensions

def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)

def register_errorhandlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, "code", 500)
        return render_template(f"errors/{error_code}.html"), error_code

    for errcode in [404, 500]:
        app.errorhandler(errcode)(render_error)
    return None

def register_blueprints(app):
    """
    Import blueprint
    Register blueprint
    """
    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp)

def create_app(config_name):
    """Create app"""
    app = Flask(__name__)
    app.config.from_object(config_options.get(config_name))

    register_extensions(app)
    register_blueprints(app)

    # if not app.debug:
    #     from flask_sslify import SSLify
    #     SSLify(app)
    
    app.wsgi_app = ProxyFix(app.wsgi_app)
    return app