from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3
def main():
    baseurl="https://movie.douban.com/top250?start="
    datalist=getdate(baseurl)
    #savedata(savepath=".\\dd.xls")
    askurl("https://movie.douban.com/top250?start=")
def getdate(baseurl):
    datelist=[]
    for i in range(0,10):
        url=baseurl+str(i*25)
        html=askurl(url)
        
    return datelist
def askurl(url):
    head={
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"
        }
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reson"):
            print(e.reason)
    return html

def savedata(savepath):
    print("save..")
if __name__=="__main__":
    main()