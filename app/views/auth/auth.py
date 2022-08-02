from flask import Blueprint, render_template, make_response, session, request

auth = Blueprint('auth', __name__, template_folder = 'templates')


@auth.route('/')
def login():
    content = dict()
    content['first_name'] = 'Sexy Ms Dollar Baby'
    content['email'] = 'kylegichez@gmail.com'
    content['amount'] = '$15,000'
    content['phone'] = '0712345678'

    template = render_template('auth/index.html', content = content)
    response = make_response(template)
    return response
