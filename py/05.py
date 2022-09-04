
import requests as rq
from basic import gethtml as gtl

utl='http://star.sse.com.cn/star/renewal/'

u=open('html/05.html','w',encoding="utf-8")

u.write(gtl(utl))