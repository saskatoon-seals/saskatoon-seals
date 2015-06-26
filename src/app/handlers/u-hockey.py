from app.handlers import BaseHandler


class UHockeyHandler(BaseHandler):
    def get(self):
        context = {}
        return self.render_response('u-hockey.html', **context)
