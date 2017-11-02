from google.appengine.ext import ndb # needed for db calls

import webapp2  # webapp2 framework
import logging  # for debugging
import json     # used to package information for sending/receiving

# a single DB entry
class NameList(ndb.Model):
    name = ndb.StringProperty()  # signer's name
    date = ndb.DateTimeProperty(auto_now_add=True)  # auto-populated; when they signed

# for webapp2: a set of handlers
class MainPage(webapp2.RequestHandler):
    def get(self):  #handles GET requests
        # this method returns a JSON object with the list of signers
        # self.response.headers['Content-Type'] = 'application/json'  # http header with content type
        # self.response.write(json.JSONEncoder.encode(self))
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<html><center<List of names<table>')   #HTML response
        query = ndb.gql("SELECT name, date FROM NameList ORDER BY date;")   # GQL query; can also use other query method
        for entry in query:
            self.response.write('<tr><td>' + entry.name + '</td><td>' + entry.date.isoformat() + '</td></tr>')
        self.response.write('<table></html>')   #close off HTML table

    def post(self): #handles POST requests
        logging.info("POST - got post") # some debugging
        logging.info("POST: payload: " + self.request.get('name'))
        entry = NameList(name=self.request.get('name')) # create entry to add to db
        entry.put() # add to db

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
