import requests
from bs4 import BeautifulSoup


def getMovie():
    # 制定请求头
    headers = {"Host": "movie.douban.com",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3760.400"}

    link = "https://movie.douban.com/top250?start="

    movie_List = []

    for i in range(0, 10):
        r = requests.get((link + str(i * 25)), headers=headers , timeout=10)
        print(str(i + 1), " 页面响应码为: ", r.status_code)
        soup = BeautifulSoup.find_all(r.text, "lxml")
        div_list = soup.find_all("div", class_="hd")
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_List.append(movie)
    print(movie_List)
    return movie_List



