from bs4 import BeautifulSoup
import requests

def judge(url):
    try:
        wb_data = requests.get(url, timeout=3)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        index = soup.find("a", "logo-2013").get('href')
        if 'http://www.zhuanzhuan.com/' in index:
            return 1
        elif 'http://www.zhuanzhuan.com/' not in index:
            return 0
        else:
            return 0
    except:
        return -1