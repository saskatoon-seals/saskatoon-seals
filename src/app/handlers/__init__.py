import json
import webapp2
from webapp2_extras import jinja2


class BaseHandler(webapp2.RequestHandler):
    """
    Base Handler
    """
    @webapp2.cached_property
    def jinja2(self):
        """
        Returns a Jinja2 renderer cached in the app registry.
        """
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        """
        Renders a template and writes the result to the response.
        """
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)

    def render_json_response(self, data):
        """
        Renders a json response
        """
        self.response.content_type = 'application/json'
        self.response.write(json.dumps(data))