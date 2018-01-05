import requests
from bs4 import BeautifulSoup
import pymongo

client = pymongo.MongoClient()
ganjiLib = client['ganjiLib']
sheet_1 = ganjiLib['sheet_1']

def ganji_or_zhzh(link):
    try:
        wb_data = requests.get(link)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        # 判断是zhuanzhuan还是ganji
        index1 = soup.find_all("div", "intro_top")
        index2 = soup.find_all("a", "logo-2013")
        if index1:
            print("zhuanzhuan")
            return 0
        elif index2:
            print("ganji")
            return 1
        else:
            print('错误链接')
            return -1
    except:
        print('错误链接')
        return -1

#print(ganji_or_zhzh('http://localhost:8888/notebooks/Untitled4.ipynb'))