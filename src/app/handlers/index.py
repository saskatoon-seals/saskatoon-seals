from app.handlers import BaseHandler


class Index(BaseHandler):
    def get(self):
        return self.redirect('u-hockey')
