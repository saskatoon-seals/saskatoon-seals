from app.handlers import BaseHandler


class Index(BaseHandler):
    def get(self):
        context = {
            'text': 'Hello Seals!'
        }
        return self.render_response('index.html', **context)
