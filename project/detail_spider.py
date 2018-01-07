# 配合main2使用
import requests
from bs4 import BeautifulSoup
import pymongo

# 激活客户端
client = pymongo.MongoClient()
new_ganjiLib = client['new_ganjiLib']
real_links = new_ganjiLib['real_links']
detail = new_ganjiLib['detail']


def insert_info(link):
    try:
        wb_data = requests.get(link, timeout=5)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        # 判断是zhuanzhuan还是ganji
        index1 = soup.find_all("div", "intro_top")
        index2 = soup.find_all("a", "logo-2013")
        if index1:  # zhuanzhuan
            print("zhuanzhuan")
            title = soup.find("h1", "info_titile").get_text().split()
            price = soup.find("span", "price_now").get_text().split()
            place = soup.find("div", "palce_li").get_text().split()
            data = {
                'title': title,
                'price': price,
                'place': place,
                'url': link
            }
            # 存入数据库
            print(data)
            detail.insert_one(data)
        elif index2:  # ganji
            print("ganji")
            title = soup.find("h1", "title-name").get_text().split()
            price = soup.find("i", "f22 fc-orange f-type").get_text().split()
            place = soup.select("ul.det-infor > li:nth-of-type(2)")[0].get_text().split()
            data = {
                'title': title,
                'price': price,
                'place': place,
                'url': link
            }
            # 存入数据库
            print(data)
            detail.insert_one(data)
    except Exception as index:
        print(index)
        return


if __name__ == '__main__':
    insert_info('http://bj.ganji.com/xuniwupin/2954374463x.htm')