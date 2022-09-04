import requests as rq
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'}

getting=rq.get('http://star.sse.com.cn/star/renewal/',headers=headers)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'}

# g2=rq.get('http://kcb.sse.com.cn/renewal/xmxq/index.shtml?auditId=632&anchor_type=0',headers=headers)
g2 = rq.get('https://eams.shanghaitech.edu.cn/eams/courseTableForStd!courseTable.action',headers=headers)
# g2=g2.text
print(getting)
print(g2)
# g2='4'
g2.encoding='utf-8'
# g2=g2.json()
g2=g2.text

g3=rq.get('https://www.zhihu.com/question/29717275',headers=headers)

print(g3)

u=open('html/zh.html','w',encoding="utf-8")

u.write(g2)
u.close()
# v=open('git02.html',)