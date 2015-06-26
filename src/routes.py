from webapp2 import Route

ROUTES = [
    Route('/', name='index', handler='app.handlers.index.Index'),
    Route('/team', name='team', handler='app.handlers.team.TeamHandler'),
    Route('/u-hockey', name='u-hockey', handler='app.handlers.u-hockey.UHockeyHandler'),
    Route('/u-football', name='u-football', handler='app.handlers.u-football.UFootballHandler'),
    Route('/calendar', name='calendar', handler='app.handlers.calendar.CalendarHandler'),
    Route('/gallery', name='gallery', handler='app.handlers.gallery.GalleryHandler'),
    Route('/contact', name='contact', handler='app.handlers.contact.ContactHandler'),
]