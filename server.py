from flask import Flask
from flask import send_file
import logging
from time import sleep
import scraper

app = Flask(__name__)

logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

@app.route('/')
def index():
    return send_file("map_history.txt")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
