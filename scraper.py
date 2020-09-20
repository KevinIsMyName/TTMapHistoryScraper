def main():
    from bs4 import BeautifulSoup
    from datetime import datetime
    import requests
    from time import sleep

    try:
        f = open("map_history.txt")
    except FileNotFoundError:
        f = open("map_history.txt", "a+")
        f.write("START\n")
        f.close

    URL = "https://www.battlemetrics.com/servers/squad/6670512"

    # This is all totally hard coded
    last_map = None
    while True:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.select("dl.css-1i1egz4")
        try:
            cur_map = str(results[1].contents[1]).strip("</dd>")
        except IndexError as e:
            print(e)
            continue

        if cur_map != last_map:
            last_map = cur_map
            with open("map_history.txt", "a+") as f:
                f.write(datetime.now().strftime(
                    "%m/%d/%Y %I:%M:%S %p") + " - " + cur_map + "\n")

        sleep(300)  # 5 minute polling rate


if __name__ == "__main__":
    main()
