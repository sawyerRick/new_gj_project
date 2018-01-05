import requests
from bs4 import BeautifulSoup
import pymongo
from checkout_404 import check_404
from add_http import add_http
from repeat_checkout import repeat_checkout

#激活mongo客户端
client = pymongo.MongoClient()
new_ganjiLib = client['new_ganjiLib']
links_lib = new_ganjiLib['links_lib']

# 爬每一类的每一页的所有链接放入数据库
def get_links_from(channel, page):
    # http://cq.ganji.com/jiaju/o15/
    # list_view ==> 对应页面的连接
    list_view = "{}o{}/".format(channel, str(page))
    try:
        wb_data = requests.get(list_view, timeout=5)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        urls = soup.select("td.t > a")
        for link in urls:
            link = link.get('href')
            link = add_http(link)
            # if repeat_checkout(link) or check_404(link):
            #     print('error_page')
            #     return
            # else:
            print(link.split('?')[0])
            links_lib.insert_one({'url': link.split('?')[0]})
    except:
        pass
    

#get_links_from("http://cq.ganji.com/rirongbaihuo/", 1)