# 抓取静态网页

import requests

r = requests.get("http://www.santostang.com/" , timeout=0.001)

print("文本编码: " , r.encoding)
print("响应状态码： " , r.status_code)
print("字符串方式的响应体： " , r.text)