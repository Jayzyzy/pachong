
import requests as rq

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36'}

# jpgurl='https://www.bing.com/images/search?q=%e7%b3%97%e4%ba%8b%e7%99%be%e7%a7%91&form=HDRSC2&first=1&tsc=ImageHoverTitle'
# jpgdata=rq.get(url=jpgurl,headers=headers).content
# import requests as rq
jpgurl='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E5%9B%BD%E5%AE%B6%E5%AE%9D%E8%97%8F%E7%94%B5%E5%BD%B1'
# jpgdata=rq.get(url=jpgurl)
jpgdata=rq.get(url=jpgurl,headers=headers)

with open('1.jpg','w+') as fp:
    fp.write(jpgdata)