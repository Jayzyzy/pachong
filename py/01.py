import urllib.request as rq

data1=rq.urlopen('http://star.sse.com.cn/star/renewal/')
print(data1.read().decode('utf-8'))