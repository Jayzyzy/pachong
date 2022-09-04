
""" 对爬虫代码进行封装 """

from email import header
from threading import local
import requests as rq 

def gethtml(url) :
    headersgethtml = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'}
    geturl = rq.get(url,headers = headersgethtml)
    geturl.encoding='uft-8'
    return(geturl.text)