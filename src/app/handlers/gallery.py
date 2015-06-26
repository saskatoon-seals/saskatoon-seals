from app.handlers import BaseHandler


class GalleryHandler(BaseHandler):
    def get(self):
        context = {}
        return self.render_response('gallery.html', **context)
