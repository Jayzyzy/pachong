
import requests as rq
import json

if __name__ == '__main__':
    # prm={
    #     'type': '24',
    #     'interval_id': '100:90 ',
    #     'action': '',
    #     'start': '1',
    #     'limit': '20',
    # }

    url1='https://movie.douban.com/typerank'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36'}
    # req=rq.get(url=url1,paraqms=prm,headers=headers)
    req=rq.get(url=url1,headers=headers)

    print(req.text)
    # ldata=req.json()
    # fp2=open('xiju.json','w+',encoding='utf-8')
    # json.dump(ldata,fp=fp2,ensure_ascii=False)
    # print('o')