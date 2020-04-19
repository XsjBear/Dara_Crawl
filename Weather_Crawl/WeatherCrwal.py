# 爬虫练习
import json
import re

import pandas as pan
import pandas as pan
import requests

'''
获取爬取的url集合
beganYear   开始年份,默认2016
endYear     结束年份,默认2019
beginMonth  开始月份,默认一月
endMonth    结束月份,默认十二月
cityId      城市id,默认深圳,59493
'''
def getCrawlUrl(beganYear = 2016 , endYear = 2019 , beginMonth =1 , endMonth = 2 , cityId = 59493):
    urls = []  #url集合
    for year in range(beganYear, endYear):
        for month in range(beginMonth, endMonth + 1):
            if year < 2016:
                urls.append('http://tianqi.2345.com/t/wea_history/js/%s_%s%s.js' % (cityId , year, month))
            elif year == 2016 :
                if month < 3 :
                    urls.append('http://tianqi.2345.com/t/wea_history/js/%s_%s%s.js' % (cityId, year, month))
                else:
                    if month < 10:
                        urls.append('http://tianqi.2345.com/t/wea_history/js/%s0%s/%s_%s0%s.js' % (year, month, cityId, year, month))
                    else:
                        urls.append('http://tianqi.2345.com/t/wea_history/js/%s%s/%s_%s%s.js' % (year, month, cityId, year, month))
            else:
               if month < 10:
                   urls.append('http://tianqi.2345.com/t/wea_history/js/%s0%s/%s_%s0%s.js' % (year, month, cityId , year, month))
               else:
                   urls.append('http://tianqi.2345.com/t/wea_history/js/%s%s/%s_%s%s.js' % (year, month, cityId , year, month))
    print(urls)
    return urls
'''
获取数据
'''
def getContent():
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'widget_dz_id=54511; widget_dz_cityValues=,; timeerror=1; defaultCityID=54511; defaultCityName=%u5317%u4EAC; Hm_lvt_a3f2879f6b3620a363bec646b7a8bcdd=1516245199; Hm_lpvt_a3f2879f6b3620a363bec646b7a8bcdd=1516245199; addFavorite=clicked',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3236.0 Safari/537.36'
    }
    content = []
    urlList = getCrawlUrl(2011 , 2019 , 1 , 12 , 57872)
    for crawlUrl in urlList:
        content.append(requests.get(crawlUrl ,  headers = headers).text + "\n")
        # print("content : ", content)
    return content


'''
数据处理
'''
def deal(content):
    all = []
    for dataMonth in content:
        print(dataMonth)
        dataMonth = dataMonth[35:str(dataMonth).index(",{}],")+1]
        dataDay = str(dataMonth).split("},")
        for dataOneDay in dataDay:
            dataOneDay = (dataOneDay + '}')
            if dataOneDay.__len__() > 4 :
                # oneDayJson = json.loads(str(dataOneDay)) #转pythondict对象
                # print(oneDayJson["ymd"])
                # print("dataOneDay : ", dataOneDay)

                one = {"year": [], "bWenDu": [], "yWenDu": [], "tianqi": [], "fengxiang": [], "fengli": [], "aqi": [],"aqiInfo": [], "aqiLeavel": []}

                ymd1 = re.findall("ymd:'(.*?)',", dataOneDay)
                bWenDu1 = re.findall("bWendu:'(.*?)℃',", dataOneDay)
                yWenDu1 = re.findall("yWendu:'(.*?)℃',", dataOneDay)
                tianqi1 = re.findall("tianqi:'(.*?)',", dataOneDay)
                fengxiang1 = re.findall("fengxiang:'(.*?)',", dataOneDay)
                fengli1 = re.findall(",fengli:'(.*?)'", dataOneDay)
                aqi1 = re.findall("aqi:'(.*?)',", dataOneDay)
                aqiInfo1 = re.findall("aqiInfo:'(.*?)',", dataOneDay)
                aqiLevel1 = re.findall(",aqiLevel:'(.*?)'", dataOneDay)

                # one = {"year": [ymd1[0]], "bWenDu": [bWenDu1[0]], "yWenDu": [yWenDu1[0]], "tianqi": [tianqi1[0]],
                #        "fengxiang": [fengxiang1[0]], "fengli": [fengli1[0]], "aqi": [aqi1[0]],
                #        "aqiInfo": [aqiInfo1[0]], "aqiLeavel": [aqiLevel1[0]]}
                # one = {}
                if ymd1.__len__() != 0:
                    one["year"].append(ymd1[0])
                else:
                    one["year"].append("")

                if bWenDu1.__len__() != 0:
                    one["bWenDu"].append(bWenDu1[0])
                else:
                    one["bWenDu"].append("")

                if yWenDu1.__len__() != 0:
                    one["yWenDu"].append(yWenDu1[0])
                else:
                    one["yWenDu"].append("")

                if tianqi1.__len__() != 0:
                    one["tianqi"].append(tianqi1[0])
                else:
                    one["tianqi"].append("")

                if fengxiang1.__len__() != 0:
                    one["fengxiang"].append(fengxiang1[0])
                else:
                    one["fengxiang"].append("")

                if fengli1.__len__() != 0:
                    one["fengli"].append(fengli1[0])
                else:
                    one["fengli"].append("")

                if aqi1.__len__() != 0:
                    one["aqi"].append(aqi1[0])
                else:
                    one["aqi"].append("")

                if aqiInfo1.__len__() != 0:
                    one["aqiInfo"].append(aqiInfo1[0])
                else:
                    one["aqiInfo"].append("")

                if aqiLevel1.__len__() != 0:
                    one["aqiLeavel"].append(aqiLevel1[0])
                else:
                    one["aqiLeavel"].append("")

                all.append(pan.DataFrame(one))
    table = pan.concat(all)
    # print(table)
    table.to_csv('衡阳2.csv', index=True)

#运行
deal(getContent())