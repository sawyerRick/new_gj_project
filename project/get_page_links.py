import requests
from bs4 import BeautifulSoup
import pymongo
from add_http import add_http
from ganji_or_zhzh import judge

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
        if judge(list_view) == 1:#判断是什么类型的网页
            urls = soup.select("td.t > a")
            for link in urls:
                link = link.get('href')  # 提取链接
                link = add_http(link)  # 修复链接格式
                if wb_data.status_code == 404:  # 404检查
                    print('404page')
                    return
                else:
                    print(link.split('?')[0])
                    links_lib.insert_one({'url': link.split('?')[0]})
        elif judge(list_view) == 0:
            urls = soup.select("dt > a > img")
            for link in urls:
                link = link.get('src')  # 提取链接
                link = add_http(link)  # 修复链接格式
                if wb_data.status_code == 404:  # 404检查
                    print('404page')
                    return
                else:
                    print(link.split('?')[0])
                    links_lib.insert_one({'url': link.split('?')[0]})
        else:
            return
    except:
        pass
    
if __name__ == '__main__':
    get_links_from("http://bj.ganji.com/ershoubijibendiannao/", 1)