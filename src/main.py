"""
Bathroom Application
"""
import os
import webapp2
from routes import ROUTES


CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
CONFIG = {
    'webapp2_extras.jinja2': {
        'template_path': os.path.join(CURRENT_PATH, 'templates'),
        'globals': {
            'uri_for': webapp2.uri_for
        }
    }
}

app = webapp2.WSGIApplication(ROUTES, debug=True, config=CONFIG)
