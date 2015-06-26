from app.handlers import BaseHandler


class ContactHandler(BaseHandler):
    def get(self):
        context = {}
        return self.render_response('contact.html', **context)
