import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com/"

# heards = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT￼ 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'widget_dz_id=54511; widget_dz_cityValues=,; timeerror=1; defaultCityID=54511; defaultCityName=%u5317%u4EAC; Hm_lvt_a3f2879f6b3620a363bec646b7a8bcdd=1516245199; Hm_lpvt_a3f2879f6b3620a363bec646b7a8bcdd=1516245199; addFavorite=clicked',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3236.0 Safari/537.36'
}

r = requests.get(link , headers = headers)
soup = BeautifulSoup(r.text , "lxml")

title = soup.find("div", class_ = "post-content").p.text.strip()
# print(title)
print(soup.prettify())


# 存储数据
with open("content.txt" ,"a+") as f:
    f.write(title)
    f.close()
