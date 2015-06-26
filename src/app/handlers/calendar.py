from app.handlers import BaseHandler


class CalendarHandler(BaseHandler):
    def get(self):
        context = {}
        return self.render_response('calendar.html', **context)
