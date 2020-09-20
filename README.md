# TTMapHistoryScraper

I made this because I don't like TacticalTriggernometry's Squad server map rotations.

## How it works

**server.py** is a Python Flask web server, only accepting one endpoint, "/". It serves the file _map_history.txt_, containing a log history of maps the TT server has run through.

**scraper.py** sends a request to battlemetrics every 5 minutes and scrapes the page for the name. Note that this is a hard-coded design, and sometimes even errors out as the response file structure is not consistent at times. I've circumvented this by catching the error and not doing anything with it. I make enough requests to battlemetrics to the point that if I get 1-2 errors, I'll be able to get a successful response that I can scrape.
