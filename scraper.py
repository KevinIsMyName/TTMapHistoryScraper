from bs4 import BeautifulSoup
import logging
import requests
from time import sleep

try:
    open("map_history.txt")
except FileNotFoundError:
    open("map_history.txt", "w")

logging.basicConfig(
    filename="map_history.txt",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

URL = "https://www.battlemetrics.com/servers/squad/6670512"

logging.debug("Executing " + __file__)

# This is all totally hard coded
last_map = None
while True:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.select("dl.css-1i1egz4")
    cur_map = str(results[1].contents[1]).strip("</dd>")

    if cur_map != last_map:
        last_map = cur_map
        logging.info(cur_map)

    sleep(300) # 5 minute polling rate
