from requests import get
from bs4 import BeautifulSoup

keyword = "Watch"
url = "https://google.com/search?q=" + keyword
raw = get(url).text
soup = BeautifulSoup(raw, 'html.parser')

with open("output1.html", "w", encoding='utf-8') as file:
    file.write(str(soup))
