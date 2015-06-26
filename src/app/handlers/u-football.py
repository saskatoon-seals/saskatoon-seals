from app.handlers import BaseHandler


class UFootballHandler(BaseHandler):
    def get(self):
        return self.redirect('https://en.wikipedia.org/wiki/Underwater_football',)
