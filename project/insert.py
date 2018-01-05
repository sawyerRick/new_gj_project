import requests
from bs4 import BeautifulSoup
from get_page_links import sheet_2
from get_page_links import ganjiLib
import pymongo

# 激活客户端
client = pymongo.MongoClient()
sheet_3 = ganjiLib['sheet_3']
sheet_4 = ganjiLib['sheet_4']
sum = sheet_2.find().count()  # 爬取的链接总数


def insert_info():
    for link in sheet_2.find().limit(sum):
        print(link)
        wb_data = requests.get(link['url'])
        soup = BeautifulSoup(wb_data.text, 'lxml')
        # 判断是zhuanzhuan还是ganji
        index1 = soup.find_all("div", "intro_top")
        index2 = soup.find_all("a", "logo-2013")
        if index1:
            print("zhuanzhuan")
            title = soup.find("h1", "info_titile").get_text().split()
            price = soup.find("span", "price_now").get_text().split()
            place = soup.find("div", "palce_li").get_text().split()
            data = {
                'title': title,
                'price': price,
                'place': place
            }
            # 存入数据库
            sheet_4.insert_one({'massages': data})
            print(data)
        elif index2:
            print("ganji")
            title = soup.find("h1", "title-name").get_text().split()
            price = soup.find("i", "f22 fc-orange f-type").get_text().split()
            place = soup.select("ul.det-infor > li:nth-of-type(2)")[0].get_text().split()
            data = {
                'title': title,
                'price': price,
                'place': place
            }
            # 存入数据库
            sheet_4.insert_one({'massages': data})
            print(data)

if __name__ == '__main__':
    insert_info()