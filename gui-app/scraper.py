import requests
from bs4 import BeautifulSoup
import time

URL = 'https://darksky.net/forecast/21.958,-159.375/us12/en'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')


def getTemp():
    low = soup.find('span', attrs={"class": "low-temp-text"})
    low = low.get_text()
    high = soup.find('span', attrs={"class": "high-temp-text"})
    high = high.get_text()
    wind = soup.find('span', attrs={"class": "num swip wind__speed__value"})
    wind = wind.get_text()
    humidity = soup.find('span', attrs={"class": "num swip humidity__value"})
    humidity = humidity.get_text()
    rain = soup.find('span', attrs={"class": "num swip"})
    rain = rain.get_text()

    print(low, high, wind, humidity, rain)
    return [low, high, wind, humidity, rain]


list = getTemp()

openFile = open('markdown.md', 'w')
for i in range(len(list)):
    openFile.write(list[i] + '\n')
openFile.close()
