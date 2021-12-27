from urllib import request
from bs4 import BeautifulSoup
# https://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp
# 전국 중기예보
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159")
# BeautifulSoup을 사용해 웹 페이지를 분석합니다.
soup = BeautifulSoup(target, "html.parser")
with open(file="k-weather.xml", mode="a") as urlPage:
    urlPage.write("{}".format(soup))
# location 태그를 찾습니다.
print(soup.select_one("author").string)

print(soup.select_one("title").string)

for item in soup.select("item"):
    # 내부의 city, wf, tmn, tmx 태그를 찾아 출력합니다.
    print(item.select_one("title").string)
    print(item.select_one("guid").string)