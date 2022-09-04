
# 爬图片
import requests as rq

if __name__ == '__main__':

    jpgurl='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E5%9B%BD%E5%AE%B6%E5%AE%9D%E8%97%8F%E7%94%B5%E5%BD%B1'
    jpgdata=rq.get(url=jpgurl).text

    with open('1.jpg','w+') as fp:
        fp.write(jpgdata)

# print('o')