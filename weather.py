import requests
import datetime
import tkinter
import re

url = "http://t.weather.sojson.com/api/weather/city/101300101"#网页链接（南宁）
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=20) #设置超时
        # 判断连接状态，为4XX或5XX时抛出异常信息
        r.raise_for_status()   
        # 将返回对象的编码格式设为响应内容编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except: #异常处理
        return "产生异常"

demo = getHTMLText(url) #调用函数

def downloadHtml(demo):
    download = open("date.text", "w")
    download.write(demo)
    download.close()
def readHtml():
    read = open("date.text", "r")
    a = read.read()
    read.close()

readHtml()

