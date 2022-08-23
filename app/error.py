from flask import render_template
from flask import current_app

@current_app.error_handler(404)
def err_404(error):
    """Error 404"""
    render_template('errors/404.html'), 404

@current_app.error_handler(500)
def err_500(error):
    """Error 500"""
    render_template('errors/500.html'), 500