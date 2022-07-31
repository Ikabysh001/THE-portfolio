import requests

from bs4 import BeautifulSoup

URL = "https://www.coingecko.com/en/coins/bitcoin"
page = requests.get(URL)




soup = BeautifulSoup(page.content, "html.parser")


p = soup.find_all("div", class_="tw-text-4xl tw-font-bold tw-my-2 tw-flex tw-items-center")

data = []

for i in p:

    data.append(i.text.strip())



print(data)


print(str(data[0])[0:7])
