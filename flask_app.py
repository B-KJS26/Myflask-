from flask import Flask, render_template
import sys
from urllib import request
from bs4 import BeautifulSoup
from flask.templating import render_template_string
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template('index.html', subject="안녕하세요. 반갑습니다. 김준서입니다.")
 
#1-1
@app.route('/show2')
def show2():
    return render_template('img_test2.html', image_file='img/2.jpg')
 
#2
@app.route("/about")
def about():
    return render_template('busan1.html')
 
#3
@app.route("/show1")
def show1():
    return render_template('img_test1.html', image_file='img/1.jpg')
 
#4
# 기상청 날씨
@app.route("/kma")
def kma():
  # urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
  target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stdId=108")
 
  # BeautifulSoup를 사용해 웹 페이지를 분석합니다.
  soup = BeautifulSoup(target, "html.parser")
 
  output = ""  
  # item 태그를 찾습니다.
  for item in soup.select("item"):
    output += "<h2>{}</h2><hr/>".format(item.select_one("title").string)
 
  # location 태그를 찾습니다.
  for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx, tmEf 태그를 찾아 출력합니다.
    output += "<h3>{}</h3>".format(location.select_one("city").string)
    output += "날씨: {}</br>".format(location.select_one("wf").string)
    output += "최저/최고 기온: {}/{}".format(location.select_one("tmn").string, location.select_one("tmx").string)
    output += "<hr/>"  
 
  output += "{}</br>".format(soup.select_one("title").string)
  output += "날짜: {}</br>".format(location.select_one("tmEf").string)  
  output += "지역: {}</br>".format(soup.select_one("province").string)
 
  return output
 
#5
@app.route("/kma1")
def kma1():
  # urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
  target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=184")
 
  # BeautifulSoup를 사용해 웹 페이지를 분석합니다.
  soup = BeautifulSoup(target, "html.parser")
 
  # location 태그를 찾습니다.
  output = ""
 
  for item in soup.select("item"):
    output += "<h2>{}</h2><hr/>".format(item.select_one("title").string)
   
  for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx, tmEf 태그를 찾아 출력합니다.
    output += "<h3>{}</h3>".format(location.select_one("city").string)
    output += "날짜: {}</br>".format(location.select_one("tmEf").string)
    output += "날씨: {}</br>".format(location.select_one("wf").string)
    output += "최저/최고 기온: {}/{}".format(location.select_one("tmn").string, location.select_one("tmx").string)
    output += "<hr/>"
 
  output += "{}</br>".format(soup.select_one("title").string)
  output += "날짜: {}</br>".format(location.select_one("tmEf").string)  
  output += "지역: {}</br>".format(soup.select_one("province").string)
 
  return output
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)