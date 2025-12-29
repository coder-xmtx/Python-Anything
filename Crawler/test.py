import requests
from bs4 import BeautifulSoup

url_toscrape = "http://books.toscrape.com/"
url_bilibili = "https://www.bilibili.com/"
url_douban = "https://movie.douban.com/top250"

# 伪装成浏览器发送GET请求，因为网页有反爬虫
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0"
}

response = requests.get(url_toscrape, headers=head)


if response.ok:
    print("请求成功", response.status_code)
else:
    print("请求失败")

# 获取网页源码
html = response.text
soup = BeautifulSoup(html, "html.parser")

# 找到所有class为price_color的p标签
all_price = soup.find_all("p", class_="price_color")
for price in all_price:
    print(price)
