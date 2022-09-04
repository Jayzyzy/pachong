
# import requests
# url = 'https://music.163.com'
# """ headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'}
# html = requests.get(url, headers=headers)
# print(html)
# print('***’)
# print(html.text)
#  """

import requests
r = requests.get('https://www.baidu.com/')
#响应内容（str类型）
print(type(r.text),r.text)
# print(r)

#响应内容（bytes类型）
# print(type(r.content),r.content)
# #状态码
# print(type(r.status_code),r.status_code)
# #响应头
# print(type(r.headers),r.headers)
# #Cookies
# print(type(r.cookies),r.cookies)
# #URL
# print(type(r.url),r.url)
# #请求历史
print(type(r.history),r.history)
u=open('gitpa/02.html','w',encoding="utf-8")

u.write(r.text)
u.close()