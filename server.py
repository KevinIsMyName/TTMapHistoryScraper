from flask import Flask
from flask import send_file
import logging
from time import sleep
import subprocess
import scraper

app = Flask(__name__)

logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

@app.before_first_request
def start_scraper():
    scraper.main()

@app.route('/')
def hello_world():
    return send_file("map_history.txt")

if __name__ == "__main__":
    app.run(host="0.0.0.0")