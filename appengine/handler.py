import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, None))

class Gallery(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'gallery/pic.html')
        self.response.out.write(template.render(path, None))

class AboutMe(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'aboutme.html')
        self.response.out.write(template.render(path, None))

class Antichess(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'antichess.html')
        self.response.out.write(template.render(path, None))

application = webapp.WSGIApplication([('/', MainPage),
                                      ('/gallery', Gallery),
                                      ('/AboutMe', AboutMe),
                                      ('/Antichess', Antichess)
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
