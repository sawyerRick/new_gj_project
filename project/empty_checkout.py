from bs4 import BeautifulSoup
import requests

def empty_checkout(link):
    wb_data = requests.get(link)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    try:
        empty_page = soup.find("div", "noinfotishi").get_text()
        if '很抱歉' in empty_page:
            return 1
        else:
            return 0
    except AttributeError:
        print('not empty page')
        return 0

empty_checkout('http://bj.ganji.com/wupinjiaohuan/o2/')

