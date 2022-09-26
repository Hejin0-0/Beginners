from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get(
    "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%82%A0%EC%94%A8&oquery=&tqi=Uz4IXwprvN8ssUW4pTKssssstvl-133166"
)
# pprint(html.text)

soup = bs(html.text, "html.parser")

data1 = soup.find("div", {"class": "detail_box"})
# pprint(data1)

data2 = data1.findAll("dd")
# pprint(data2)

fine_dust = data2[0].find("span", {"class": "num"}).text
print(fine_dust)

ultra_fine_dust = data2[1].find("span", {"class": "num"}).text
print(ultra_fine_dust)
