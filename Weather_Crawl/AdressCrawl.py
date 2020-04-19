# encoding = utf-8
# 城市地址编码爬取

import requests
import re

# url:http://tianqi.2345.cn/static/js/citySelectData.js

# 城市编码js文件url
url = "http://tianqi.2345.cn/static/js/citySelectData.js"

# 获取数据
def getContent(url):
    # 模拟浏览器访问,设置访问头
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'widget_dz_id=54511; widget_dz_cityValues=,; timeerror=1; defaultCityID=54511; defaultCityName=%u5317%u4EAC; Hm_lvt_a3f2879f6b3620a363bec646b7a8bcdd=1516245199; Hm_lpvt_a3f2879f6b3620a363bec646b7a8bcdd=1516245199; addFavorite=clicked',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3236.0 Safari/537.36'
    }
    # 通过url获取数据
    content = requests.get(url, headers=headers).text
    return content  # 返回内容

# 城市数据处理
def dearContent():
    print(getContent(url))
    result = re.findall("('|')", getContent(url))
    print(result)
    pass


dearContent()