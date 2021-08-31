import requests
from bs4 import BeautifulSoup
import re

query = "twitter"
search = query.replace(" ", "+")
results = 15
url = f"https://www.google.com/search?q={search}&num={results}"
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'authority': 'www.google.com'
    }


requests_results = requests.get(url, headers=headers)
soup_link = BeautifulSoup(requests_results.content, "html.parser")
with open("som.html", "w") as f:
    f.write(str(soup_link))
links = soup_link.find_all("a")

for link in links:
    print("AA")
    link_href = link.get("href")
    print(link_href)
    if "url?q=" in link_href and not "webcache" in link_href:
        title = link.find_all("h3")

        if len(title) > 0:
            print(link.get("href").split("?q=")[1].split("&sa=U")[0])
            # print(title[0].getText())
            print("------")
